# from databricks.connect import DatabricksSession
import ibis

def get_product_counts():
    # spark = DatabricksSession.builder.remote(serverless=True).getOrCreate()
    con = ibis.databricks.connect(server_hostname="TODO.cloud.databricks.com", http_path="/sql/1.0/warehouses/TODO")
    QUERY = """
        with products (product_id, price) as (
            select 'p1', 5
            union all
            select 'p2', 10
        )
        select
            count(*) as total,
            count(*) filter (
                where price > 5
            ) as expensive_count
        from products
    """
    # df = spark.sql(QUERY)
    # df.show(10)
    result = con.sql(QUERY).execute()
    print(result)

