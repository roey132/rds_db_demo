output "db_host" {
  value = aws_db_instance.postgres.address
}

output "db_name" {
  value = var.db_name
}

output "db_user" {
  value = var.db_user
}

output "db_port" {
  value = aws_db_instance.postgres.port
}
