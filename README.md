# Grafana StreamX: ETL and Visualization Project

## Overview

Grafana StreamX is a project designed to automate the process of extracting data from multiple CSV files, loading the data into a PostgreSQL database, and visualizing it using Grafana. This project leverages Apache Airflow for orchestration, Docker Compose for containerization, and Grafana for monitoring and visualization.

## Project Structure

- **src/**: Contains the main Python scripts for the ETL (Extract, Transform, Load) process.
- **data/**: Directory where the CSV files are stored.
- **dags/**: Directory for Airflow DAGs (Directed Acyclic Graphs).
- **config/**: Configuration files for Airflow and other services.
- **plugins/**: Custom plugins for Airflow.
- **logs/**: Log files generated by Airflow.
- **Dockerfile**: Dockerfile for building the Python script container.
- **docker-compose.yml**: Docker Compose configuration file to set up the entire environment.
- **.env**: Environment file for storing environment variables.

## Prerequisites

- **Docker** and **Docker Compose**: Ensure Docker and Docker Compose are installed on your system.
- **Python 3.9**: The project is built using Python 3.9.
- **CSV Data**: Place your CSV files in the `data/` directory.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/grafanastreamx.git
cd grafanastreamx
```

### 2. Environment Configuration

Ensure that the `.env` file is correctly set up with the necessary environment variables, such as `AIRFLOW_UID`, `AIRFLOW_PROJ_DIR`, and database credentials.

### 3. Docker Compose

Build and run the Docker containers using Docker Compose:

```bash
docker-compose build
docker-compose up -d
```

This command will start the following services:
- **PostgreSQL**: Database to store the extracted data.
- **Redis**: Message broker for Airflow’s Celery executor.
- **Apache Airflow**: For orchestrating the ETL process.
- **Python Script Container**: Executes the ETL process to load data from CSV files into PostgreSQL.
- **Grafana**: Visualizes the data stored in PostgreSQL.

### 4. Load Data into PostgreSQL

The Python script in the `src/` directory will automatically extract data from the CSV files in the `data/` directory and load it into the PostgreSQL database. This process is orchestrated by Airflow.

### 5. Access Grafana

Once the data is loaded, you can access Grafana to create dashboards and visualize the data:

- **Grafana URL**: [http://localhost:3000](http://localhost:3000)
- **Default Login**: `admin/admin`

### 6. Airflow Dashboard

Monitor and manage your DAGs (ETL workflows) using the Airflow web UI:

- **Airflow URL**: [http://localhost:8089](http://localhost:8089)
- **Default Login**: `airflow/airflow`

### 7. Customizing the Project

- **ETL Script**: Modify the Python script in `src/main.py` to customize how the data is processed and loaded into PostgreSQL.
- **Airflow DAGs**: Create or modify DAGs in the `dags/` directory to define new workflows.
- **Grafana Dashboards**: Create custom dashboards in Grafana to visualize your data.

## Data Flow

1. **Extraction**: Python scripts in the `src/` directory read data from CSV files stored in the `data/` directory.
2. **Transformation**: Data is processed and transformed as needed within the Python scripts.
3. **Loading**: Transformed data is loaded into PostgreSQL.
4. **Visualization**: Grafana visualizes the data, allowing users to create custom dashboards and monitor the data in real-time.

## Troubleshooting

- **Container Logs**: Use `docker logs <container_name>` to check the logs for each service.
- **Airflow Issues**: Check the Airflow logs in the `logs/` directory for any issues with the DAGs.
- **Database Issues**: Ensure PostgreSQL is running and accessible via the connection details provided in the `.env` file.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Apache Airflow**: For orchestration.
- **Grafana**: For powerful data visualization.
- **Docker**: For containerization and easy deployment.
- **PostgreSQL**: As the relational database management system.
- **Redis**: For message brokering.

---

Feel free to modify this `README.md` as per your project’s specific needs. This document provides a comprehensive guide to setting up, running, and customizing your ETL and visualization pipeline with Grafana, Airflow, and PostgreSQL.