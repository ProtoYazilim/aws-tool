import argparse
from ec2_manager import EC2Manager


def main():
    parser = argparse.ArgumentParser(description="List EC2 instances by region.")
    parser.add_argument('--region', type=str, help="Specify an AWS region, e.g., us-east-1")
    args = parser.parse_args()

    manager = EC2Manager(region=args.region)
    manager.run()


if __name__ == '__main__':
    main()