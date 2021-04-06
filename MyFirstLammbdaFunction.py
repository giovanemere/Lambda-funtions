def lambda_handler(event, context):
    print("In lambda habdler")

    resp = {
        "statusCode": 200,
        "headers": {
            "Acces-Control-Allow-Origin": "*"   ,
        },
        "body": "Edisson Zuñiga"
    }

    return resp