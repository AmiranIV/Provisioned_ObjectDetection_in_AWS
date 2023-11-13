## Provisioned well architected Object Detection Service in AWS

![botaws4](https://github.com/AmiranIV/Provisioned_ObjectDetection_in_AWS/assets/109898333/36f4263e-bce3-4140-bbec-388c4fc31928)

Project Overview:
The project involves building a robust Object Detection Service in AWS, comprising several key components.

Infrastructure Requirements:

VPC and Subnets: Establish a VPC with a minimum of two public subnets.
Polybot Microservice: Run the Polybot service within a micro EC2 instance using Docker. Create an AMI for future instance launches. Ensure high availability using an Application Load Balancer (ALB) across different AZs, employing HTTPS and managing access using security groups.
Telegram Access: Allow traffic only from specified Telegram servers to the ALB.
Security Measures:

Sensitive Data Handling: Store the Telegram token in AWS Secret Manager.
TLS Certificates: Implement HTTPS using a self-signed certificate or a registered domain with ACM.
Yolo5 Microservice Integration:

Service Deployment: Set up the Yolo5 service in a similar configuration to Polybot, utilizing Docker and integrating with other services.
Communication Flow: Establish communication between Polybot and Yolo5 via SQS, S3, and DynamoDB, allowing the exchange of data and results.
Auto-Scaling: Implement an AutoscalingGroup for the Yolo5 service based on the volume of messages in the SQS queue.
Scaling Metrics and Management:

metricStreamer Microservice: Introduce a new microservice to calculate BacklogPerInstance, enabling the AutoscalingGroup to dynamically adjust the Yolo5 instances based on the queue workload, ensuring efficient resource allocation.
This architecture aims for a scalable and efficient Object Detection Service on AWS, integrating multiple services and enabling automatic scaling based on queue workload metrics.

