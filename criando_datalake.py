import boto3
from botocore.exceptions import ClientError
import logging


# Função para criar um bucket 
def create_bucket(bucket_name , region= None):

    # Criando o S bucket 
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)

    except ClientError as e:
        logging.error(e)
        return False
    
    return True


def main():

        # Criando o Bucket no s3 da Aws
        if create_bucket("datalake-henry-enem"):
            print("Bucket Criado com sucesso")
        


        # Criando um client s3
        s3_client = boto3.client('s3')

        # Realizando uma solicitação dos buckets existentes
        response = s3_client.list_buckets()

        # Output dos buckets presentes
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')


        # Inserindo os dados na camada raw_data
        s3_client.upload_file("enem2020/DADOS/MICRODADOS_ENEM_2020.csv", 
                                "datalake-henry-enem",
                                "raw_data/enem/enem=2020/MICRODADOS_ENEM_2020.csv")


if __name__ == "__main__":

    main()