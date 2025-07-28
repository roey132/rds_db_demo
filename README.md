# RDS Data Warehouse Demo

This project provisions an AWS PostgreSQL database using Terraform and loads a sample dataset into a star-schema data warehouse. Python scripts apply database migrations and load CSV files into staging and warehouse tables.

## Requirements

Before starting, ensure the following tools and accounts are available:

- **AWS account** with permissions to create VPCs, security groups and an RDS instance.
- **AWS CLI** installed and configured locally (`aws configure`).
- **Terraform** v1 or later installed.
- **Python 3** with `pip`.

Python dependencies are listed in `requirements.txt` and include `psycopg2-binary`, `python-dotenv` and `yoyo-migrations`.

## Project Structure

- `data/` – CSV files that will be loaded into the staging tables.
- `load_scripts/` – Python scripts to load data into staging and then into warehouse tables.
- `sql/` – SQL migration files and transformation scripts.
- `terraform/` – Terraform configuration that creates the AWS infrastructure.

## Setup

1. **Clone the repository** and install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure AWS credentials** so Terraform can provision resources:

   ```bash
   aws configure
   ```

3. **Set a database password** in `terraform/terraform.tfvars`:

   ```hcl
   db_password = "your_password_here"
   ```

4. **Initialize and apply Terraform** from the `terraform` directory:

   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

   Terraform creates the VPC, subnets, security group and RDS PostgreSQL instance. After completion it outputs values such as `db_host`, `db_name`, `db_user` and `db_port`.

5. **Create a `.env` file** in the repository root using the Terraform outputs:

   ```bash
   DB_HOST=<value of db_host>
   DB_NAME=<value of db_name>
   DB_USER=<value of db_user>
   DB_PASSWORD=<value used in terraform.tfvars>
   DB_PORT=<value of db_port>
   ```

## Running the Database Setup

With the infrastructure in place and environment variables configured, run the following commands from the repository root:

1. **Apply the database migrations** to create tables and indexes:

   ```bash
   python sql/migrations.py
   ```

2. **Load the CSV files into the staging schema:**

   ```bash
   python load_scripts/load_to_stg.py
   ```

3. **Transform the data into the warehouse tables:**

   ```bash
   python load_scripts/load_to_dwh.py
   ```

After these steps the RDS database contains populated dimensional and fact tables.

## Clean Up

To remove all AWS resources created by Terraform, run from the `terraform` directory:

```bash
terraform destroy
```

## Notes

The dataset provided in `data/` originates from the Olist e-commerce public dataset. The Terraform configuration opens the RDS instance to the internet for demonstration purposes. In a production setting you should restrict access to specific IPs or networks. link to data: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
