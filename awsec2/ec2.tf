terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  profile = "default"
}

variable "vpc_id" {
}
variable "subnet_id" {
}
//security.tf
resource "aws_security_group" "allInSsh" {
  name   = "allow-all-sg"
  vpc_id = var.vpc_id
  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
  }
  // Terraform removes the default rule
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "testserver" {
  ami             = "ami-053b0d53c279acc90"
  instance_type   = "t2.micro"
  key_name        = "test"
  security_groups = ["${aws_security_group.allInSsh.id}"]
  subnet_id       = var.subnet_id
  tags = {
    Name = "ExampleAppServerInstance"
  }
}

output "public_ip" {
  value = aws_instance.testserver.public_ip
}
