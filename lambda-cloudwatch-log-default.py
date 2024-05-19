import logging
import os
import boto3

# Configure logging
logger = logging.getLogger()
logging.basicConfig(format="%(asctime)s %(message)s")
logger.setLevel(logging.getLevelName(os.getenv("logger_level", "DEBUG")))

log_client = boto3.client("logs", region_name=os.getenv("AWS_REGION"))
default_log_retention = int(os.getenv("default_log_retention", 365))


def get_log_group_name() -> list[str]:
    log_groups = []
    log_paginator = log_client.get_paginator("describe_log_groups")
    for page in log_paginator.paginate():
        for log_group in page["logGroups"]:
            retention_in_days = log_group.get("retentionInDays", None)
            if retention_in_days is None or retention_in_days > default_log_retention:
                log_groups.append(log_group["logGroupName"])
    return log_groups


def lambda_handler(event, context) -> None:
    """
    Lambda function handler for setting default retention policy for CloudWatch log groups.
    """
    logger.info(f"Recieved event: {event}")
    event_source = event.get("eventSource", None)
    if event_source != "logs.amazonaws.com":
        for log_group_name in get_log_group_name():
            logger.info(f"Setting default retention policy for log group: {log_group_name}")
            log_client.put_retention_policy(logGroupName=log_group_name, retentionInDays=default_log_retention)
        return

    log_group_name = event["requestParameters"].get("logGroupName", None)
    retention_in_days = event["requestParameters"].get("retentionInDays", None)

    if (retention_in_days is None) or (retention_in_days > default_log_retention):
        logger.info(f"Setting default retention policy for log group: {log_group_name}")
        log_client.put_retention_policy(logGroupName=log_group_name, retentionInDays=default_log_retention)

    return
