Create a new experiment in the `exp_load_balancing` directory with the following requirements:
- Use Infrastructure as Code with Cloud Formation.
- Use both Application LB and Network LB.
- In case of using Network LB, connect it with another Application LB, to illustrate the flexibility of LB.
- In order to use a LB, I assume that we need some target group, let's use Sticky Session with 1 target group at least.
- Implement some endpoints in Python to handle the request actually.
- If you need security group, IAM, or anything necessary, create them as well.