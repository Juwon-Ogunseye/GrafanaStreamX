from airflow import DAG
from airflow.operators.bash import BashOperator  # Updated import
from datetime import datetime, timedelta

default_args = {
    'owner': 'juwon',
    'start_date': datetime.today(),  # Set the start date to today
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'test_dag',
    default_args=default_args,
    schedule=timedelta(minutes=1),  # Updated parameter name
    catchup=False,
)

# Modify the command with the path to your Python script
command ="//wsl.localhost/Ubuntu/home/juwon/airflow-docker/dags/ohh_script.py"
  # Updated script path

# Create a BashOperator to execute the Python script
run_script = BashOperator(
    task_id='run_script',
    bash_command=command,
    dag=dag,
)

# Set the task dependencies
run_script

if __name__ == "__main__":
    dag.cli()