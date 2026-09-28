import snowflake.connector
from snowflake.core import Root
from snowflake.core.compute_pool import ComputePool

with snowflake.connector.connect(connection_name="tutorial") as conn:
    root = Root(conn)

    compute_pool = ComputePool(
        name="MY_COMPUTE_POOL",
        instance_family="CPU_X64_XS",
        min_nodes=1,
        max_nodes=1,
        auto_suspend_secs=300,
    )

    root.compute_pools.create(
        compute_pool,
        mode="ifnotexists",
    )

    print("Compute pool creation completed!")