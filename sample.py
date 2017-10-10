# -*- coding: utf-8 -*-

import botocore
import boto3
import io

# Refs : https://boto3.readthedocs.io/en/latest/reference/services/s3.html

s3 = boto3.client('s3')

def main():

    # [追加する時]
    # バケットがなければ作成
    # あればそれを使う。
    # ファイルの重複チェック
    # 重複していれば、削除し更新
    # 重複していなければ追加。

    # [読み込み]
    # ファイルを読み込む

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

    # if isExistBucketFor(bucketName):
    #     print('Delet bucket...')
    #     response = s3.delete_bucket( Bucket='bun-chan-bot-images')
    #     print(response)
    # else:
        # print('Create bucket...')
        # response = s3.create_bucket(
        #     Bucket='bun-chan-bot-images',
        #     CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-1'}
        # )

    objectName = 'image.jpg'

    if isExistObjectFor(bucketName, objectName):
        print("{name} already exist.".format(name=objectName))

        print("Delete {objectName}.".format(objectName=objectName))
        s3.delete_object(Bucket=bucketName, Key=objectName)

        print("Re-Upload {objectName} to {bucketName}.".format(bucketName=bucketName, objectName=objectName))
        with open('./image.jpg', 'rb') as fh:
            s3.upload_fileobj(fh, bucketName, objectName)

    else:
        print("Upload {objectName} to {bucketName}.".format(bucketName=bucketName, objectName=objectName))
        with open('./image.jpg', 'rb') as fh:
            s3.upload_fileobj(fh, bucketName, objectName)

def isExistObjectFor(bucketName, objectName):
    try:
        s3.head_object(Bucket=bucketName, Key=objectName)
        return True
    except botocore.exceptions.ClientError as e:
        print(e)
        return False

def isExistBucketFor(bucketName):
    try:
        response = s3.head_bucket(Bucket=bucketName)
        # response = s3.head_bucket(Bucket='test-lambda-on-java')
        print(response)
        return True

    except botocore.exceptions.ClientError as e:
        print("The {bucketName} does not found".format(bucketName=bucketName))
        print(e)

        return False

if __name__ == '__main__':
    main()