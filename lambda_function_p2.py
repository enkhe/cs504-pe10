# Part 2 – Creating an AWS Lambda
# CS504-PE10 - Enkh B
# AWS Lambda Functions URL: https://us-east-2.console.aws.amazon.com/lambda/home?region=us-east-2#/functions/calculate_age?subtab=url&tab=code

import json
import datetime

def lambda_handler(event, context):
    query_params = event.get('queryStringParameters') or {}
    
    query_param_birth_year = int(query_params['birth_year'])
    query_param_birth_month = int(query_params['birth_month'])
    query_param_birth_day = int(query_params['birth_day'])
    
    age = calculate_age(query_param_birth_year, query_param_birth_month, query_param_birth_day)
    
    # For plain text like your example: Your age is: 27
    result = f"Your age is: {age}"
    
    return {
        'statusCode': 200,
        'headers': { 'Content-Type': 'text/plain' },
        'body': result
        # If you want JSON, use this instead:
        # 'body': json.dumps({"age": age, "message": result})
    }
	
def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.date.today()
    
    # Handle Feb 29 birthdays in non-leap years (counts Feb 28 as birthday)
    try:
        birthday_this_year = datetime.date(today.year, birth_month, birth_day)
    except ValueError:
        # birth_day is 29 Feb and this year is not leap year
        birthday_this_year = datetime.date(today.year, 2, 28)

    age = today.year - birth_year - (today < birthday_this_year)
    return age


###
Status: Succeeded
Test Event Name: test_calculate_age

Response:
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "text/plain"
  },
  "body": "Your age is: 35"
}

The area below shows the last 4 KB of the execution log.

Function Logs:
START RequestId: 1a6587b5-04aa-4f04-8ae7-181683d430c1 Version: $LATEST
END RequestId: 1a6587b5-04aa-4f04-8ae7-181683d430c1
REPORT RequestId: 1a6587b5-04aa-4f04-8ae7-181683d430c1	Duration: 2.65 ms	Billed Duration: 117 ms	Memory Size: 128 MB	Max Memory Used: 38 MB	Init Duration: 113.46 ms

Request ID: 1a6587b5-04aa-4f04-8ae7-181683d430c1

###
