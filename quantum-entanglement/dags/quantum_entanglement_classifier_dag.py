from airflow.decorators import dag, task
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import uuid

# Default arguments for the DAG
default_args = {
    'owner': 'faical',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
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
    witness_names = ['CHSH', 'CONCURRENCE', 'ENTROPY', 'NEGATIVITY', 'CHSH_OPTIMAL', 'PPT']

    for witness_name in witness_names:
        
        @task
        def generate_airflow_dag_run_id():
            return str(uuid.uuid4())

        airflow_dag_run_id = generate_airflow_dag_run_id()

        # Task to run the simulation
        run_simulation_task = DockerOperator(
            task_id=f'run_simulation-{witness_name}',
            image='ghcr.io/guybrush007/quantum-entanglement:0.4.0',
            api_version='auto',
            auto_remove=True,
            command=(
                f"papermill /home/jovyan/00-Simulation.ipynb /home/jovyan/EXECUTED-00-Simulation-{witness_name}.ipynb -p WITNESS_NAME {witness_name} -p SIMULATION_PATH /home/jovyan -p AIRFLOW_DAG_RUN_ID {airflow_dag_run_id} -p MLFLOW_URL http://localhost:5000"
            ),
            docker_url='unix://var/run/docker.sock',
            network_mode='host',
            mount_tmp_dir=False,
        )

        # Task to run the training
        run_training_task = DockerOperator(
            task_id=f'run_training-{witness_name}',
            image='ghcr.io/guybrush007/quantum-entanglement:0.4.0',
            api_version='auto',
            auto_remove=True,
            command=(
                f"papermill /home/jovyan/01-Training.ipynb /home/jovyan/EXECUTED-01-Training-{witness_name}.ipynb -p WITNESS_NAME {witness_name} -p AIRFLOW_DAG_RUN_ID {airflow_dag_run_id} -p MLFLOW_URL http://localhost:5000"
            ),
            docker_url='unix://var/run/docker.sock',
            network_mode='host',
            mount_tmp_dir=False,
        )

        # Task to run prediction 
        run_predict_task = DockerOperator(
            task_id=f'run_predict-{witness_name}',
            image='ghcr.io/guybrush007/quantum-entanglement:0.4.0',
            api_version='auto',
            auto_remove=True,
            command=(
                f"papermill /home/jovyan/02-Predict.ipynb /home/jovyan/EXECUTED-02-Predict-{witness_name}.ipynb -p WITNESS_NAME {witness_name} -p AIRFLOW_DAG_RUN_ID {airflow_dag_run_id} -p MLFLOW_URL http://localhost:5000"
            ),
            docker_url='unix://var/run/docker.sock',
            network_mode='host',
            mount_tmp_dir=False,
        )

        airflow_dag_run_id >> run_simulation_task >> run_training_task >> run_predict_task

dag = quantum_entanglement_classifier_ml_pipeline()
