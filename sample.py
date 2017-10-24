# -*- coding: utf-8 -*-

import botocore
import boto3
import io
from datetime import datetime
import s3Uploader

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


    # if isExistBucketFor(bucketName):
    # else:
    #     print('Delet bucket...')
    #     response = s3.delete_bucket( Bucket='bun-chan-bot-images')
    #     print(response)
        # print('Create bucket...')
        # response = s3.create_bucket(
        #     Bucket='bun-chan-bot-images',
        #     CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-1'}
        # )

    bucketName = 'bun-chan-bot-images'
    objectName = "image_{name}.jpg".format(name=datetime.now().strftime("%Y%m%d_%H%M%S"))

    uploader = s3Uploader.s3Uploader(bucketName, objectName, './image.jpg')
    uploader.upload()


if __name__ == '__main__':
    main()