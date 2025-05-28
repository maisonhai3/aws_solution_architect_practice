import os
import json
import boto3
import logging
from botocore.config import Config
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Environment variables set by CloudFormation
APPCONFIG_APPLICATION_ID = os.environ.get('APPCONFIG_APPLICATION_ID')
APPCONFIG_ENVIRONMENT_ID = os.environ.get('APPCONFIG_ENVIRONMENT_ID')
APPCONFIG_CONFIG_PROFILE_ID = os.environ.get('APPCONFIG_CONFIG_PROFILE_ID')

# CloudWatch metric namespace and names
METRIC_NAMESPACE = 'HelloApiTelemetry'
METRIC_TOTAL_CALLS = 'HelloEndpointCalls'
METRIC_IS_WORLD_TRUE = 'HelloEndpointIsWorldTrue'

# AppConfig client
appconfigdata = boto3.client('appconfigdata', config=Config(retries={'max_attempts': 2}))
cloudwatch = boto3.client('cloudwatch')

def get_is_world_flag():
    """
    Fetch the is_world flag from AWS AppConfig.
    """
    try:
        # Start configuration session
        session = appconfigdata.start_configuration_session(
            ApplicationIdentifier=APPCONFIG_APPLICATION_ID,
            EnvironmentIdentifier=APPCONFIG_ENVIRONMENT_ID,
            ConfigurationProfileIdentifier=APPCONFIG_CONFIG_PROFILE_ID
        )
        token = session['InitialConfigurationToken']
        config_response = appconfigdata.get_latest_configuration(
            ConfigurationToken=token
        )
        content = config_response['Configuration'].read()
        config_json = json.loads(content)
        return config_json.get('is_world', True)
    except Exception as e:
        logger.error(f"Error fetching AppConfig: {e}")
        # Default to True if AppConfig fails
        return True

def put_metric(metric_name, value=1):
    try:
        cloudwatch.put_metric_data(
            Namespace=METRIC_NAMESPACE,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Value': value,
                    'Unit': 'Count'
                }
            ]
        )
    except Exception as e:
        logger.error(f"Error putting CloudWatch metric {metric_name}: {e}")

def handler(event, context):
    # Telemetry: count every call
    put_metric(METRIC_TOTAL_CALLS)

    # Get is_world flag from AppConfig
    is_world = get_is_world_flag()

    # Telemetry: count is_world=true
    if is_world:
        put_metric(METRIC_IS_WORLD_TRUE)

    # Response logic
    name = "world" if is_world else "me"
    body = f"Hello, {name}"
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": body
    }
