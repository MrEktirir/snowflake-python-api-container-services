import snowflake.connector
from textwrap import dedent

from snowflake.core import Root
from snowflake.core.service import Service, ServiceSpecInlineText

with snowflake.connector.connect(connection_name="tutorial") as conn:
    root = Root(conn)

    schema = root.databases["SPCS_PYTHON_API_DB"].schemas["PUBLIC"]

    image_repository = schema.image_repositories["MY_IMAGE_REPOSITORY"]

    specification = dedent(f"""\
    spec:
      containers:
      - name: web-server
        image: {image_repository.fetch().repository_url}/nginx:latest
      endpoints:
      - name: ui
        port: 80
        public: true
    """)

    service = Service(
        name="MY_NGINX_SERVICE",
        compute_pool="MY_COMPUTE_POOL",
        spec=ServiceSpecInlineText(spec_text=specification),
        min_instances=1,
        max_instances=1,
    )

    schema.services.create(service, mode="ifnotexists")

    print("Service creation completed!")