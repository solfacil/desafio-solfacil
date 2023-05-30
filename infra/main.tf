terraform {
  cloud {
    organization = "phraulino"

    workspaces {
      name = "challenge-workspace"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "api_security_group" {
  name        = "api_security_group"
  description = "Security Group for API"

  ingress {
    from_port   = var.pgadmin_port
    to_port     = var.pgadmin_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = var.api_port
    to_port     = var.api_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "ec2_instance" {
  ami                    = "ami-053b0d53c279acc90" # AMI ID da região escolhida
  instance_type          = "t2.micro"
  key_name               = "api_challenge" # Nome da chave SSH que você possui
  vpc_security_group_ids = [aws_security_group.api_security_group.id]

  user_data = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y docker.io docker-compose

    # Clonar o repositório com o docker-compose.yml
    git clone https://github.com/PHRaulino/challenge-ph.git ${var.api_repo_path}
    cd ${var.api_repo_path}
    rm -f .env
    touch .env
    # Definir as variáveis de ambiente
    echo "POSTGRES_USER=${var.postgres_user}" >> ${var.api_repo_path}/.env
    echo "POSTGRES_PASS=${var.postgres_pass}" >> ${var.api_repo_path}/.env
    echo "POSTGRES_DB=${var.postgres_db}" >> ${var.api_repo_path}/.env
    echo "POSTGRES_HOST=${var.postgres_host}" >> ${var.api_repo_path}/.env
    echo "POSTGRES_PORT=${var.postgres_port}" >> ${var.api_repo_path}/.env
    echo "PGADMIN_EMAIL=${var.pgadmin_email}" >> ${var.api_repo_path}/.env
    echo "PGADMIN_PASS=${var.pgadmin_pass}" >> ${var.api_repo_path}/.env
    echo "PGADMIN_PORT=${var.pgadmin_port}" >> ${var.api_repo_path}/.env
    echo "API_PORT=${var.api_port}" >> ${var.api_repo_path}/.env
    echo "API_HOST=${var.api_host}" >> ${var.api_repo_path}/.env

    # Executar o Docker Compose com as variáveis de ambiente
    docker-compose up -d
    EOF

  tags = {
    Name = "EC2_Challenge"
  }
}

output "instance_url" {
  value = aws_instance.ec2_instance.public_ip
}

output "instance_id" {
  value = aws_instance.ec2_instance.id
}
