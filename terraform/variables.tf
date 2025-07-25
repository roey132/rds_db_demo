variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "db_identifier" {
  type    = string
  default = "olist-dwh-db"
}

variable "db_name" {
  type    = string
  default = "olistdb"
}

variable "db_user" {
  type    = string
  default = "olistadmin"
}

variable "db_password" {
  type    = string
  sensitive = true
}
