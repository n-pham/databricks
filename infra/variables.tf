variable "databricks_host" {
  description = "Databricks workspace URL"
  type        = string
}

variable "databricks_token" {
  description = "Databricks personal access token"
  type        = string
  sensitive   = true
}

variable "databricks_username" {
  description = "Databricks username"
  type        = string
}