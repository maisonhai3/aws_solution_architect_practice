FROM public.ecr.aws/lambda/python:3.11

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy app
COPY app.py ./

# Set the CMD to your handler
CMD ["app.lambda_handler"]
