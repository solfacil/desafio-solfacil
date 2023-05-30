variable "postgres_user" {
  description = "this is the user of the database"
  type        = string
  default     = "user"
}
variable "postgres_pass" {
  description = "this is the password of the user database"
  type        = string
  default     = "password"
}
variable "postgres_db" {
  description = "this is the name of the database"
  type        = string
  default     = "challenge_database"
}
variable "postgres_host" {
  description = "this is the name of the service in docker-compose.yml"
  type        = string
  default     = "challenge_db"
}
variable "postgres_port" {
  description = "this is the port of the database"
  type        = string
  default     = "5432"
}
variable "pgadmin_email" {
  description = "this is the email of the pgadmin user"
  type        = string
  default     = "sample@challenge.com"
}
variable "pgadmin_pass" {
  description = "this is the password of the pgadmin user"
  type        = string
  default     = "password"
}
variable "pgadmin_port" {
  description = "this is the port of the pgadmin"
  type        = string
  default     = "8080"
}
variable "api_port" {
  description = "this is the port of the api"
  type        = string
  default     = "5001"
}
variable "api_host" {
  description = "this is the host of the api"
  type        = string
  default     = "0.0.0.0"
}
variable "api_repo_path" {
  description = "this is the host of the api"
  type        = string
  default     = "/home/ubuntu/challenge"
}
