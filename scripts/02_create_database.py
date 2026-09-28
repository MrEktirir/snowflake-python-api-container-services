import snowflake.connector
from snowflake.core import Root
from snowflake.core.database import Database

with snowflake.connector.connect(
    connection_name="tutorial"
) as conn:

    root = Root(conn)

    database = Database(
        name="SPCS_PYTHON_API_DB"
    )

    root.databases.create(
        database,
        mode="ifnotexists"
    )

    print("Database creation completed!")