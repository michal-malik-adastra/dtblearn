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

test = BashOperator(
    task_id='test',
    bash_command='/home/airflow/venv/bin/dbt test --select tag:tag_test --project-dir /home/airflow/dtblearn',
    dag=dag
)

test_all = BashOperator(
    task_id='test_all',
    bash_command='/home/airflow/venv/bin/dbt test --project-dir /home/airflow/dtblearn',
    dag=dag
)

start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

start_task >> test >> test_all >> end_task
