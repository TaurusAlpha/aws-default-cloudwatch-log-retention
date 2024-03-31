import logging
import os
import boto3
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_boto3_logs import CloudWatchLogsClient

# Configure logging
logger = logging.getLogger()
log_level_name = os.getenv(
    "logger_level", "DEBUG"
)  # Fetch the log level name from the environment
log_level = getattr(
    logging, log_level_name.upper(), logging.DEBUG
)  # Convert to logging level, defaulting to DEBUG

logging.basicConfig(level=log_level, format="%(asctime)s %(message)s")


def lambda_handler(event, context) -> None:
    """
    Lambda function handler for setting default retention policy for CloudWatch log groups.
    """
    log_client: CloudWatchLogsClient = boto3.client("logs")
    default_log_retention = os.environ.get("default_log_retention", 365)
    log_group_name = event["requestParameters"]["logGroupName"]

    if "retentionInDays" not in event["requestParameters"]:
        logger.info(f"Setting default retention policy for log group: {log_group_name}")
        log_client.put_retention_policy(
            logGroupName=log_group_name, retentionInDays=int(default_log_retention)
        )
