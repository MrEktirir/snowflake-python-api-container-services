import snowflake.connector
from snowflake.core import Root

with snowflake.connector.connect(
    connection_name="tutorial"
) as conn:

    root = Root(conn)

    databases = root.databases.iter(
        like="SPCS_PYTHON_API_DB"
    )

    for database in databases:
        print("Database exists:", database.name)