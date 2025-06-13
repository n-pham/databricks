from databricks.connect import DatabricksSession

def main():
    spark = DatabricksSession.builder.remote(serverless=True).getOrCreate()
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
    df = spark.sql(QUERY)
    df.show(10)

if __name__ == "__main__":
    main()
