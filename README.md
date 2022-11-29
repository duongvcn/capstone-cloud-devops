# Capstone Cloud DevOps

# Project Overview
- This is capstone project for Udacity devops course.
- This is a simple pipeline using CircleCI for deploy a static HTML project

# Requirements
- CircleCI
- AWS EKS (Kubernetes)
- circleci/aws-eks@2.2.0
- circleci/kubernetes@1.3
- Create the CircleCI account
- Create the DockerHub account
- Create a GitHub repository

# Add the AWS credentials as environment variables
- AWS_ACCESS_KEY_ID	
- AWS_DEFAULT_REGION	
- AWS_SECRET_ACCESS_KEY
- AWS_SESSION_TOKEN	
- DOCKER_PASSWORD
- DOCKER_USERNAME
- 

# Create EKS cluster  
- Create EKS role name eksClusterRole: https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html#create-service-role

- Create EKS Cluster name: aws-devops
# Pipeline steps
- run-lint
- build-docker-image
- push-docker-image
- build-and-push-image-ecr
- deploy-application
- test-application
- set-loadbalancer




