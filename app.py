import boto3 dev
client = boto3.client('ec2')
response = client.run_instances(
    ImageId ='ami-0453ec754f44f9a4a',
    InstanceType = 't2.micro',
    KeyName='pem',
    MaxCount=1,
    MinCount=1,
)
