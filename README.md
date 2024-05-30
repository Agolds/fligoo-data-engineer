# fligoo-data-engineer

Pre-Requisites:
1. Docker
2. Code editor
3. Git (to clone repo)
4. Register in Aviationstack API and replace ACCESS_KEY with your personal access key in the CONSTANTS file.
  -  http://api.aviationstack.com/
  -  CONSTANT key: FLIGHTS_API_ACCESS_KEY_FILTERS

Steps:
1. Run command: 'docker-compose up --build' in terminal. This will turn the container on and build the image.
2. Open: http://0.0.0.0:8080/ in web browser. This will open the Airflow UI on the login page.
3. Login to Airflow: User/Pass --> admin/admin.
4. Access DAG: 'ETL_FLIGHTS_DATA_FLIGOO'.
5. Turn it on and track logs in run_etl task.
6. Check whether failed or succeeded based on logs in the'Log' section of the task.
7. While docker container is up, you can validate loaded data by:
  - Accessing JupyterNotebooks folder in repo and there are available analtycs queries to run. Simply use an IDE to run the file or connect to Jupyter if needed.
  - Create or modify queries as needed.
