# ECS Hello World with Telemetry and CI/CD

This experiment provisions an ECS service behind an Application Load Balancer, with CI/CD using CodePipeline and CodeBuild. Each visit to the API endpoint is counted and recorded to S3 for telemetry analysis.

## Structure
- `cloudformation.yaml`: Provisions ALB, ECS, S3, CodePipeline, CodeBuild, IAM roles, etc.
- `app/`: Simple Flask app that counts visits and writes telemetry to S3.
- `README.md`: This file.

## Usage
1. Deploy the CloudFormation stack.
2. Push code to the repository to trigger the pipeline.
3. Visit the ALB endpoint to generate telemetry.
4. Check S3 for telemetry data.
