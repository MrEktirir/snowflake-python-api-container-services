import snowflake.connector
from snowflake.core import Root
from snowflake.core.image_repository import ImageRepository

with snowflake.connector.connect(connection_name="tutorial") as conn:
    root = Root(conn)

    schema = root.databases["SPCS_PYTHON_API_DB"].schemas["PUBLIC"]

    image_repository = ImageRepository(name="MY_IMAGE_REPOSITORY")

    schema.image_repositories.create(
        image_repository,
        mode="ifnotexists"
    )

    print("Image repository creation completed!")