# CloudWatch Logs Retention Policy Setter

This project provides an AWS CloudFormation template for automatically setting retention policies for CloudWatch Log Groups across all AWS Organization accounts. It utilizes a Lambda function triggered by CloudWatch Event Rules to apply a default retention policy to any new or existing log group without a defined retention period.

## Description

The provided CloudFormation stack deploys the following resources:
- An IAM Role for the Lambda function execution with the necessary permissions.
- A Lambda function that sets the default retention period for CloudWatch Log Groups.
- CloudWatch Event Rule to trigger the Lambda function on log group creation or deletion of retention policy.

The Lambda function uses environment variables to determine the default retention period and the log level for its own execution logs.

## Features

- **Automatic Retention Policy Application:** Automatically applies a default retention policy to CloudWatch Log Groups.
- **Flexible Retention Periods:** Supports a range of retention periods from 1 day to up to 10 years.
- **Configurable Log Level:** Allows setting the log level of the Lambda function for better control over logging verbosity.

## Prerequisites

- AWS Account with access to CloudFormation, IAM, Lambda, and CloudWatch.
- Proper IAM permissions to deploy CloudFormation stacks.

## Deployment

1. Navigate to the AWS CloudFormation console.
2. Choose 'Create stack' > With new resources (standard).
3. Upload the provided CloudFormation template file.
4. Specify stack details as required, including parameters for the default log retention period and Lambda log level.
5. Acknowledge that the stack might create IAM resources and choose 'Create stack'.

## Usage

Once deployed, the system works automatically. It will set the specified default retention period to any CloudWatch Log Group created within the AWS Organization that does not already have a retention policy defined.

### Parameters

- `DefaultLogRetention`: The default retention period for CloudWatch log groups in days. (Default: 365)
- `LambdaLogLevel`: Log level for the Lambda function. (Default: "INFO")

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

