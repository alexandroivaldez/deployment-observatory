variable "aws_region" {
  description = "AWS region to deploy into"
  default     = "us-east-1"
}

variable "app_name" {
  description = "Name used across all resources"
  default     = "deployment-observatory"
}