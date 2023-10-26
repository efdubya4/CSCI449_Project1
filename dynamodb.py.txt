import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
     AttributeDefinitions=[
        {
            'AttributeName': 'ipAddress',
            'AttributeType': 'S'
        }
    ],
    TableName='ipAddresses_v1',
    KeySchema=[
        {
            'AttributeName': 'ipAddress',
            'KeyType': 'HASH'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 8,
        'WriteCapacityUnits': 8
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)