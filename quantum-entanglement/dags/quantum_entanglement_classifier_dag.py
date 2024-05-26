from airflow.decorators import dag
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'faical',
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
    description='Run simulations and neural network trainings for Quantum entangled states'
)
def quantum_entanglement_classifier_ml_pipeline():
    witness_names = ['CHSH', 'CONCURRENCE', 'ENTROPY', 'NEGATIVITY']

    for witness_name in witness_names:
        run_simulation_task = DockerOperator(
            task_id=f'run_simulation-{witness_name}',
            image='ghcr.io/guybrush007/quantum-entanglement:0.0.5', 
            api_version='auto',
            auto_remove=False,
            command=f"papermill /home/jovyan/00-Simulation.ipynb /home/jovyan/EXECUTED-00-Simulation-{witness_name}.ipynb -p WITNESS_NAME {witness_name} -p SIMULATION_PATH /home/jovyan",
            docker_url='unix://var/run/docker.sock',
            network_mode='host',
        )

        run_training_task = DockerOperator(
            task_id=f'run_training-{witness_name}',
            image='ghcr.io/guybrush007/quantum-entanglement:0.0.5', 
            api_version='auto',
            auto_remove=False,
            command=f"papermill /home/jovyan/01-Training.ipynb /home/jovyan/EXECUTED-01-Training-{witness_name}.ipynb -p WITNESS_NAME {witness_name}",
            docker_url='unix://var/run/docker.sock',
            network_mode='host',
        )

        run_simulation_task >> run_training_task

dag = quantum_entanglement_classifier_ml_pipeline()