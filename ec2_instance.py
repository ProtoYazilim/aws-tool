

class EC2Instance:

    def __init__(self, instance):
        self.name = self._get_instance_name(instance)
        self.instance_id = instance.get('InstanceId', 'N/A')
        self.instance_type = instance.get('InstanceType', 'N/A')
        self.instance_state = instance['State']['Name']
        self.public_ip = instance.get('PublicIpAddress', 'N/A')
        self.elastic_ip = self._get_elastic_ip(instance)

    def _get_instance_name(self, instance):
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    return tag['Value']
        return 'N/A'

    def _get_elastic_ip(self, instance):
        if 'NetworkInterfaces' in instance:
            for interface in instance['NetworkInterfaces']:
                if 'Association' in interface and 'PublicIp' in interface['Association']:
                    return interface['Association']['PublicIp']
        return 'N/A'

    def display_info(self):
        return f"{self.name}\t{self.instance_id}\t{self.instance_state}\t{self.instance_type}\t{self.public_ip}\t{self.elastic_ip}"

