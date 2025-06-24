from dagster import asset
from project.extract.product import get_product_counts

@asset
def product_counts():
    get_product_counts()

@asset(deps=[product_counts])
def clean_up():
    print("Clean up")
