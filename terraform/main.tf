terraform {
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 5.0"
      }
    }

    backend "s3" {
    bucket         = "deployment-observatory-tfstate"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}

provider "aws" {
    region = var.aws_region
}

resource "aws_ecr_repository" "main" {
  name = var.app_name
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_dynamodb_table" "deploys" {
  name = "deploys"
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "deploy_id"

  attribute {
    name = "deploy_id"
    type = "S"
  }
}