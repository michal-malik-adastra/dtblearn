from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 19),
    'email': [],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

dag = DAG(
    dag_id='airbnb_run',
    default_args=default_args,
    description='This dag runs data analytics on top of netflix datasets',
    schedule_interval=None,
    catchup=False
)
    
run_dimensions = BashOperator(
    task_id='run_dimensions',
    bash_command='/home/airflow/venv/bin/dbt run --select tag:tag_dim --project-dir /home/airflow/dtblearn > /home/airflow/custom.log',
    dag=dag
)

run_facts = BashOperator(
    task_id='run_facts',
    bash_command='/home/airflow/venv/bin/dbt run --select tag:tag_fct --project-dir /home/airflow/dtblearn > /home/airflow/custom.log',
    dag=dag
)

seed = BashOperator(
    task_id='seed',
    bash_command='/home/airflow/venv/bin/dbt seed --project-dir /home/airflow/dtblearn > /home/airflow/custom.log',
    dag=dag
)

run_fullmoon = BashOperator(
    task_id='run_fullmoon_mart',
    bash_command='/home/airflow/venv/bin/dbt run --select tag:tag_fullmoon_mart --project-dir /home/airflow/dtblearn > /home/airflow/custom.log',
    dag=dag
)

start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

start_task >> run_dimensions >> run_facts >> run_fullmoon >> end_task
start_task >> seed >> run_fullmoon
