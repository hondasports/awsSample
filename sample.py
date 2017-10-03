# -*- coding: utf-8 -*-

import botocore
import boto3

# Refs : https://boto3.readthedocs.io/en/latest/reference/services/s3.html

s3 = boto3.client('s3')

def main():

    # response = s3.delete_bucket( Bucket='bun-chan-bot-images')
    # print(response)

    # response = s3.create_bucket(
    #     Bucket='bun-chan-bot-images',
    #     CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-1'}
    #     )
    # print(response)

    # response = None

    # response = s3.list_buckets()

    # # 指定したBucketが存在しなければ例外発生する。確認用に使える。
    # try:
    #     response = s3.head_bucket(Bucket='bun-chan-bot-images')
    #     # response = s3.head_bucket(Bucket='test-lambda-on-java')
    #     print(response)

    # except botocore.exceptions.ClientError as e:
    #     print('The bucket does not found')
    #     print(e)

    # response = s3.head_bucket(Bucket='bun-chan-bot-images')
    # print(response)
    
    # for bucket in response['Buckets']:
    #     print(bucket.get('Name'))
    #     if bucket.get('Name') != 'bun-chan-bot-images':
    #         print('Not Found')

    bucketName = 'bun-chan-bot-images'

    if isExistBucketFor(bucketName) == False:
        print('Create bucket...')
        response = s3.create_bucket(
            Bucket='bun-chan-bot-images',
            CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-1'}
        )

        with open('./image.jpg', 'rb') as fh:
            s3.upload_fileobj(fh, bucketName, "image.jpg")

    else:
        print('Delet bucket...')
        response = s3.delete_bucket( Bucket='bun-chan-bot-images')
        print(response)
        

def isExistBucketFor(bucketName):
    try:
        response = s3.head_bucket(Bucket='bun-chan-bot-images')
        # response = s3.head_bucket(Bucket='test-lambda-on-java')
        print(response)
        return True

    except botocore.exceptions.ClientError as e:
        print('The bucket does not found')
        print(e)

        return False

if __name__ == '__main__':
    main()