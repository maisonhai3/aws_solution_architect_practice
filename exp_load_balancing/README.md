# Load Balancing Experiment

This experiment provisions both an Application Load Balancer (ALB) and a Network Load Balancer (NLB) using AWS CloudFormation. The NLB forwards traffic to the ALB, which then routes requests to EC2 instances running a simple Python Flask app. Sticky sessions are enabled on the ALB target group.

## Files
- `cloudformation-load-balancing.yaml`: CloudFormation template for all AWS resources.
- `app/handler.py`: Python Flask app with endpoints for testing.
- `app/requirements.txt`: Python dependencies.

## Usage
1. Deploy the CloudFormation stack, providing your VPC and subnet IDs.
2. The stack will launch an EC2 instance, ALB, NLB, and all required IAM and security groups.
3. Access the endpoints via the ALB or NLB DNS names (see stack outputs).

## Endpoints
- `/` - Returns a hello message.
- `/health` - Health check endpoint for the load balancer.
- `/sticky` - Returns sticky session info (cookie-based).

## Notes
- Update the AMI ID in the template as needed for your region.
- The EC2 instance pulls the app from a GitHub repo; update the repo URL if needed.
