from fastapi import FastAPI, Request
import boto3
import os
from datetime import datetime
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

cloudwatch = boto3.client('cloudwatch')
namespace = os.environ.get('CW_METRIC_NAMESPACE', 'ECSHelloWorldTelemetry')


@app.get("/")
async def hello(request: Request):
    # Put custom metric to CloudWatch
    cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': 'Visit',
                'Dimensions': [
                    {'Name': 'Path', 'Value': '/'},
                ],
                'Value': 1,
                'Unit': 'Count',
                'Timestamp': datetime.utcnow()
            }
        ]
    )
    return PlainTextResponse('Hello, World! Visit recorded.')


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000)
