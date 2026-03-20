output "app_url" {
  description = "The live URL of your deployment observatory"
  value       = "http://${aws_lb.main.dns_name}"
}

output "ecr_repo_url" {
  description = "ECR repository URL for pushing Docker images"
  value       = aws_ecr_repository.main.repository_url
}