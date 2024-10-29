# awsRegionInstanceListing

## Overview

`awsRegionInstanceListing` is a Python-based application designed to retrieve and display information about all EC2 instances within a specified AWS region, or across all regions if no region is specified. The application uses **AWS SDK** (`boto3`) to communicate with AWS services and **Poetry** to manage dependencies and environment isolation.

## Key Features

- Lists EC2 instances in a specified region or all regions.
- Displays key information for each instance:
  - **Name**
  - **Instance ID**
  - **Instance State**
  - **Instance Type**
  - **Public IPv4 Address**
  - **Elastic IP** (if assigned)

## Project Structure

- **`app.py`**: The main entry point that initiates the EC2 listing process.
- **`ec2_instance.py`**: Defines the `EC2Instance` class, representing an individual EC2 instance.
- **`ec2_manager.py`**: Contains the `EC2Manager` class, responsible for connecting to AWS, retrieving instance data, and displaying it.

## Requirements

- **Python 3.8+**
- **AWS CLI** configured with credentials and permissions to access EC2 instances.
- **Poetry** for dependency management and environment setup.

## Setup and Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/{organizationName}/awsRegionInstanceListing.git
   cd awsRegionInstanceListing


2. **List Instances in a Specific Region**:

    ```bash
    python app.py --region us-east-1
   
    #List Instances Across All Regions (if no --region argument is provided):
    python app.py