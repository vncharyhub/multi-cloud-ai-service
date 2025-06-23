# Multi-Cloud AI Service Pipeline

## 🚀 Overview
This serverless application routes prompts to either Amazon Bedrock or Azure OpenAI. Deployed using AWS CodePipeline and CloudFormation.

## 🧱 Architecture Diagram

[Insert your architecture diagram here]

## 📁 Tech Stack
- AWS Lambda (Python)
- API Gateway (HTTP API)
- AWS CodePipeline
- AWS Secrets Manager
- GitHub (Source Control)

## 🛠️ Setup Instructions

### 1. Clone the repo and set GitHub secrets:
Set the following parameters when deploying:
- GitHubOwner
- GitHubRepo
- GitHubBranch
- GitHubToken (as a parameter or in AWS Secrets Manager)

### 2. Deploy CloudFormation stack:

```bash
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name MultiCloudAIStack \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    GitHubOwner=<your-username> \
    GitHubRepo=<your-repo> \
    GitHubToken=<your-token>
