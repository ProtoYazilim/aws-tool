import boto3
from ec2_instance import EC2Instance
from botocore.config import Config


class EC2Manager:
    def __init__(self, region=None):
        self.config = Config(
            retries={'max_attempts': 10, 'mode': 'standard'},
            connect_timeout=60,
            read_timeout=60
        )
        self.region = region

    def get_all_regions(self):
        ec2 = boto3.client('ec2', config=self.config)
        response = ec2.describe_regions()
        return [region['RegionName'] for region in response['Regions']]

    def fetch_instances(self, region):
        ec2 = boto3.client('ec2', region_name=region, config=self.config)
        try:
            response = ec2.describe_instances()
        except Exception as e:
            print(f"Error fetching instances in {region}: {e}")
            return []

        instances = []
        for reservation in response['Reservations']:
            for instance_data in reservation['Instances']:
                instances.append(EC2Instance(instance_data))

        return instances

    def display_instances(self, instances):
        print("Name\tInstance ID\tState\tType\tPublic IP\tElastic IP")
        for instance in instances:
            print(instance.display_info())

    def run(self):
        regions = [self.region] if self.region else self.get_all_regions()

        for region in regions:
            print(f"\nEC2 Instances in region: {region}")
            instances = self.fetch_instances(region)
            if instances:
                self.display_instances(instances)
            else:
                print(f"No instances found in {region}.")
