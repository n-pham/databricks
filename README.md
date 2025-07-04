Testing Databricks

# Set up

* Install Databricks CLI
* Configure
   ```bash
   databricks configure
   ```
* Infra

   [Install OpenTofu](https://opentofu.org/docs/intro/install/standalone)

   Create file dev.tfvars

      databricks_host = "https://<workspace>.cloud.databricks.com"
      databricks_token = "<Settings - Developer - Access tokens>"
      databricks_username = "user@example.com"

   tofu init

   tofu plan -var-file=dev.tfvars

   tofu apply -var-file=dev.tfvars