import logging
import os
import boto3
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_logs import CloudWatchLogsClient

# Configure logging
logging.basicConfig(format="%(asctime)s %(message)s",level=logging.getLevelName(os.getenv("logger_level", "DEBUG")))
logger = logging.getLogger()


def lambda_handler(event, context) -> None:
    """
    Lambda function handler for setting default retention policy for CloudWatch log groups.
    """
    logger.info(f"Recieved event: {event}")
    log_client: CloudWatchLogsClient = boto3.client("logs", region_name=os.getenv("AWS_REGION"))
    default_log_retention = int(os.getenv("default_log_retention", 365))
    log_group_name = event["requestParameters"]["logGroupName"]

    if "retentionInDays" not in event["requestParameters"]:
        logger.info(f"Setting default retention policy for log group: {log_group_name}")
        log_client.put_retention_policy(
            logGroupName=log_group_name, retentionInDays=default_log_retention
        )
