import boto3
import time

# Your configuration settings
AUTOSCALING_GROUP_NAME = 'ASG-Yolov-AmiranIV-Worker'
QUEUE_NAME = 'AmiranIV-AWS-Queue'
namespace = 'Yolo5Metrics'  

while True:
    # Initialize AWS clients
    sqs_client = boto3.resource('sqs', region_name='eu-north-1')
    asg_client = boto3.client('autoscaling', region_name='eu-north-1')
    cloudwatch_client = boto3.client('cloudwatch', region_name='eu-north-1')

    # Get queue attributes
    queue = sqs_client.get_queue_by_name(QueueName=QUEUE_NAME)
    msgs_in_queue = int(queue.attributes.get('ApproximateNumberOfMessages'))

    # Get Auto Scaling Group information
    asg_groups = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[AUTOSCALING_GROUP_NAME])[
        'AutoScalingGroups']

    if not asg_groups:
        raise RuntimeError('Autoscaling group not found')
    else:
        asg_size = asg_groups[0]['DesiredCapacity']

    # Check if there are instances in the ASG before dividing
    if asg_size > 0:
        backlog_per_instance = msgs_in_queue / asg_size
    else:
        backlog_per_instance = 0  # Set a default value or handle this case as needed

    # Send backlog_per_instance to CloudWatch
    metric_name = 'BacklogPerInstance'
    dimensions = [
        {
            'Name': 'AutoScalingGroupName',
            'Value': AUTOSCALING_GROUP_NAME
        }
    ]

    response = cloudwatch_client.put_metric_data(
        Namespace=namespace,
        MetricData=[
            {
                'MetricName': metric_name,
                'Dimensions': dimensions,
                'Value': backlog_per_instance,
                'Unit': 'None'  
            }
        ]
    )

    print(f'Sent {metric_name} metric to CloudWatch with value: {backlog_per_instance}')

    # Sleep for 30 seconds before running the loop again
    time.sleep(30)
