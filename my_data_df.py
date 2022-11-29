# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jV1Ux2vpJqCaTYwxV5Na3nfHFM8VmtjV
"""

import os
# Find the latest version of spark 3.0 from http://www.apache.org/dist/spark/ and enter as the spark version
# For example:
# spark_version = 'spark-3.0.3'
spark_version = 'spark-3.1.3'
os.environ['SPARK_VERSION']=spark_version

# Install Spark and Java
!apt-get update
!apt-get install openjdk-11-jdk-headless -qq > /dev/null
!wget -q http://www.apache.org/dist/spark/$SPARK_VERSION/$SPARK_VERSION-bin-hadoop2.7.tgz
!tar xf $SPARK_VERSION-bin-hadoop2.7.tgz
!pip install -q findspark

# Set Environment Variables
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = f"/content/{spark_version}-bin-hadoop2.7"

# Start a SparkSession
import findspark
findspark.init()

!wget https://jdbc.postgresql.org/download/postgresql-42.2.16.jar

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("CloudETL").config("spark.driver.extraClassPath","/content/postgresql-42.2.16.jar").getOrCreate()

# Read in data from S3 Buckets
from pyspark import SparkFiles
url ="https://mypostbucket43.s3.amazonaws.com/user_data.csv"
spark.sparkContext.addFile(url)
user_data_df = spark.read.csv(SparkFiles.get("user_data.csv"), sep=",", header=True, inferSchema=True)

# Show DataFrame
user_data_df.show()

url ="https://mypostbucket43.s3.amazonaws.com/user_payment.csv"
spark.sparkContext.addFile(url)
user_payment_df = spark.read.csv(SparkFiles.get("user_payment.csv"), sep=",", header=True, inferSchema=True)

# Show DataFrame
user_payment_df.show()

joined_df=user_data_df.join(user_payment_df, on="username", how="inner")
joined_df.show()

dropna_df=joined_df.dropna()
dropna_df.show()

from pyspark.sql.functions import col

cleaned_df = dropna_df.filter(col("active_user") ==True)
cleaned_df.show()

clean_user_df = cleaned_df.select(["id", "first_name", "last_name", "username"])
clean_user_df.show()

cleaned_billing_df = cleaned_df.select(["billing_id", "street_address", "state", "username"])
cleaned_billing_df.show()

cleaned_payment_df = cleaned_df.select(["billing_id", "cc_encrypted"])
cleaned_payment_df.show()

# Store environmental variable
from getpass import getpass
password = getpass('enter password')
# Configure settings for RDS
mode = "append"
jdbc_url="jdbc:postgresql://mypostdata.chfkgfjojbdv.us-east-1.rds.amazonaws.com:5432/my_data_class_db"
config = {"user":"postgres",
          "password": password,
          "driver":"org.postgresql.Driver"}

# Write DataFrame to active_user table in RDS
clean_user_df.write.jdbc(url=jdbc_url, table='active_user', mode=mode, properties=config)

# Write dataframe to billing_info table in RDS
cleaned_billing_df.write.jdbc(url=jdbc_url, table='billing_info', mode=mode, properties=config)

# Write dataframe to payment_info table in RDS
cleaned_payment_df.write.jdbc(url=jdbc_url, table='payment_info', mode=mode, properties=config)