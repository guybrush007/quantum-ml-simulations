from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import papermill as pm

def run_simulation(**kwargs):
    witness_name = kwargs['params']['WITNESS_NAME']
    pm.execute_notebook(
        '00-Simulation.ipynb',
        './executed_notebooks/00-Simulation-{}.ipynb'.format(witness_name),
        parameters={'WITNESS_NAME': witness_name}
    )

def run_training(**kwargs):
    witness_name = kwargs['params']['WITNESS_NAME']
    pm.execute_notebook(
        '01-Training.ipynb',
        './executed_notebooks/01-Training-{}.ipynb'.format(witness_name),
        parameters={'WITNESS_NAME': witness_name}
    )

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'Quantum_Entanglement_Classifier_ML_pipeline',
    default_args=default_args,
    description='Run simulations and neural network trainings for Quantum entangled states',
    schedule_interval='@daily'
)

witness_names = ['CHSH', 'CONCURRENCE', 'ENTROPY', 'NEGATIVITY']

for witness_name in witness_names:
    run_simulation_task = PythonOperator(
        task_id='run_simulation-{}'.format(witness_name),
        python_callable=run_simulation,
        op_kwargs={'WITNESS_NAME': witness_name},
        dag=dag,
    )

    run_training_task = PythonOperator(
        task_id='run_training-{}'.format(witness_name),
        python_callable=run_training,
        op_kwargs={'WITNESS_NAME': witness_name},
        dag=dag,
    )

    run_simulation_task >> run_training_task 

