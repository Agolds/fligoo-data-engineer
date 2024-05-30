from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from scripts.etl.main.main import main
# from airflow.operators.email_operator import EmailOperator


default_args = {
    'owner': 'alex',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}


with DAG(
    dag_id='ETL_FLIGHTS_DATA_FLIGOO',
    default_args=default_args,
    description='A simple ETL DAG that runs a Python script and sends an email notification',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
) as dag:
    run_etl = PythonOperator(
        task_id='run_etl',
        provide_context=True,
        python_callable=main,
        # os.getenv('AIRFLOW_VAR_APP_SCRIPT_PATH')
        op_kwargs={"project_main_path": '/opt/airflow/scripts/etl/main/main.py'},
        dag=dag
    )

    run_etl

    # Access email settings from environment variables
    # smtp_to = os.getenv('SMTP_TO')
    # smtp_mail_from = os.getenv('AIRFLOW__SMTP__SMTP_MAIL_FROM')

    # send_success_email = EmailOperator(
    #     task_id='send_success_email',
    #     to=smtp_to,
    #     subject='Data Pipeline "Flight tracking data" finished successfully',
    #     html_content='The ETL DAG has been completed successfully.',
    #     trigger_rule='all_success',
    #     from_email=smtp_mail_from
    # )
    #
    # send_failure_email = EmailOperator(
    #     task_id='send_failure_email',
    #     to=smtp_to,
    #     subject='Data Pipeline "Flight tracking data" finished with ERROR',
    #     html_content='The ETL DAG has failed.',
    #     trigger_rule='one_failed',
    #     from_email=smtp_mail_from
    # )
