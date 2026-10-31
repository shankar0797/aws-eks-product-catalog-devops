variable "aws_region" {
  description = "AWS region for the Product Catalog project"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Name used to identify project resources"
  type        = string
  default     = "product-catalog"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "availability_zones" {
  description = "Two Availability Zones for the project"
  type        = list(string)

  validation {
    condition     = length(var.availability_zones) == 2
    error_message = "Exactly two Availability Zones must be provided."
  }
}