
from __future__ import print_function
import time
import os
import sys
import aws_encryption_sdk
import boto3

s3 = boto3.client('s3')
s3_bucket_name = os.environ['s3_BUCKET_NAME ']
kms_key = os.environ['KMS CUSTOMER KEY']

kms_kwargs = dict(key_ids = [kms_key])
master_key_provider = aws_encryption_sdk.KMSMasterKeyProvider(**kms_kwargs)

def encrypt(plaintext, botocore_session = None):
    #encrypt file

    ciphertext, encryption_header = aws_encryption_sdk.encrypt(
        plain = plaintext,
        key_provider = master_key_provider
    )

    print('storing encrypt data in s3 bucket')

    response = s3.put_object(
        body = ciphertext,
        Bucket = s3_bucket_name,
        key = "encrypted_file.txt"
    )


encrypt()
