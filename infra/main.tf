terraform {
  required_providers {
    databricks = {
      source = "databricks/databricks"
    }
  }
}

provider "databricks" {
  host  = var.databricks_host
  token = var.databricks_token
}

resource "databricks_notebook" "example_notebook" {
  path     = "/Users/${var.databricks_username}/hello_databricks_notebook"
  language = "PYTHON"
  content_base64 = base64encode(file("${path.module}/../notebooks/hello_databricks_notebook.py"))
}