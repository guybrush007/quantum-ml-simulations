from airflow.decorators import dag, task
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime, timedelta
import uuid

# Default arguments for the DAG
default_args = {
    'owner': 'admin',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    dag_id='quantum_entanglement_classifier_ml_pipeline',
    default_args=default_args,
    schedule_interval=None,
    description='Run simulations and neural network trainings for Quantum entangled states',
    catchup=False
)
def quantum_entanglement_classifier_ml_pipeline():
    witness_names = ['CHSH', 'CONCURRENCE', 'ENTROPY', 'NEGATIVITY']

    for witness_name in witness_names:
        
        @task
        def generate_airflow_dag_run_id():
            return str(uuid.uuid4())

        airflow_dag_run_id = generate_airflow_dag_run_id()

        # Task to run the simulation
        run_simulation_task = KubernetesPodOperator(
            task_id=f'run_simulation-{witness_name}',
            name=f'run-simulation-{witness_name}',
            namespace='airflow',
            image='ghcr.io/guybrush007/quantum-entanglement:0.1.1',
            cmds=["papermill"],
            arguments=[
                "/home/jovyan/00-Simulation.ipynb",
                f"/home/jovyan/EXECUTED-00-Simulation-{witness_name}.ipynb",
                "-p", "WITNESS_NAME", witness_name,
                "-p", "SIMULATION_PATH", "/home/jovyan",
                "-p", "AIRFLOW_DAG_RUN_ID", airflow_dag_run_id,
                "-p", "MLFLOW_URL", "http://mlflow.mlflow:5000"
            ],
            is_delete_operator_pod=False,
            get_logs=True,
        )

        # Task to run the training
        run_training_task = KubernetesPodOperator(
            task_id=f'run_training-{witness_name}',
            name=f'run-training-{witness_name}',
            namespace='airflow',
            image='ghcr.io/guybrush007/quantum-entanglement:0.1.1',
            cmds=["papermill"],
            arguments=[
                "/home/jovyan/01-Training.ipynb",
                f"/home/jovyan/EXECUTED-01-Training-{witness_name}.ipynb",
                "-p", "WITNESS_NAME", witness_name,
                "-p", "AIRFLOW_DAG_RUN_ID", airflow_dag_run_id,
                "-p", "MLFLOW_URL", "http://mlflow.mlflow:5000"
            ],
            is_delete_operator_pod=False,
            get_logs=True,
        )

        airflow_dag_run_id >> run_simulation_task >> run_training_task

dag = quantum_entanglement_classifier_ml_pipeline()