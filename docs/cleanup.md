\# AWS Resource Cleanup



\## Purpose



This guide describes how to remove the AWS resources created for the Product Catalog DevOps lab and reduce ongoing charges.



\## Important Warnings



\- Confirm that the resources belong to this project before deleting them.

\- Save the final project evidence and verify the GitHub push first.

\- Do not delete Terraform state before Terraform-managed infrastructure has been destroyed successfully.

\- Review every Terraform destroy plan before approval.

\- Resources created outside Terraform must be inspected and cleaned up separately.



\## 1. Remove the Kubernetes Ingress



From an authorized Kubernetes client, inspect the Ingress:



```powershell

kubectl get ingress

kubectl describe ingress

```



Delete the project Ingress using its actual name:



```powershell

kubectl delete ingress product-catalog-ingress

```



Wait for the associated ALB to be deleted. Verify the load balancer is gone in the AWS console or using AWS CLI.



\## 2. Review Kubernetes Resources



Inspect project-specific resources:



```powershell

kubectl get deployments

kubectl get services

kubectl get hpa

kubectl get pods

kubectl get ingress

```



If deleting the cluster immediately afterward, Kubernetes resources will be removed with the cluster. Remove standalone components installed outside Terraform where appropriate.



\## 3. Review Terraform Infrastructure



From the repository root:



```powershell

terraform -chdir=terraform validate

terraform -chdir=terraform plan -destroy

```



Read the entire destroy plan. Confirm it targets only the intended lab resources.



If the plan is correct, execute:



```powershell

terraform -chdir=terraform destroy

```



Review the confirmation prompt before approving.



Do not remove the Terraform state or local Terraform directory until destruction has completed and you have verified the results.



\## 4. Inspect Resources Created Outside Terraform



Check for remaining project resources, including:



\- Application Load Balancers and target groups

\- Elastic IP addresses and NAT Gateways

\- ECR images and repositories

\- IAM roles and customer-managed policies

\- GitHub OIDC provider and role

\- AWS Load Balancer Controller IAM resources

\- CloudWatch log groups

\- EBS volumes and snapshots



Delete only resources confirmed to belong to this lab and no longer needed.



\## 5. Verify Cleanup



Check the AWS console and CLI for remaining resources in `ap-south-1`.



Confirm that:



\- The EKS cluster and managed node group are gone.

\- The NAT Gateway and Elastic IP are released.

\- The project ALB and target groups are gone.

\- The project ECR repository is removed if no longer needed.

\- No unattached billable resources remain.



Some AWS resources may take time to finish deleting. Recheck any resource that is still in a deleting state.



\## 6. Final Repository Safety



Never commit:



\- Terraform state files

\- `terraform.tfvars`

\- AWS access keys or secrets

\- Local Terraform provider directories

\- Temporary credentials or authentication backups



Keep useful `.tf` configuration files and sanitized project documentation in GitHub.
