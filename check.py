from sqlalchemy import create_engine, inspect

# Use service name 'postgres' for the database URL
DATABASE_URL = 'postgresql://airflow:airflow@172.26.0.3:5432/airflow'


# Create a connection to the PostgreSQL database
engine = create_engine(DATABASE_URL)

# Inspect the database to list all tables
inspector = inspect(engine)
tables = inspector.get_table_names()

if not tables:
    print("No tables found in the database.")
else:
    print("Tables in the database:")
    for table in tables:
        print(table)
