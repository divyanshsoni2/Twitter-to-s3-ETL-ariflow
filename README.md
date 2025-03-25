# 🚀 Twitter ETL Pipeline with Airflow & AWS S3

This project demonstrates a complete **ETL (Extract, Transform, Load)** data pipeline built using **Apache Airflow**, designed to extract tweets from the **Twitter API**, transform them into a structured format, and load the final dataset into an **Amazon S3 bucket**.

---

## 📌 Project Highlights

- ✅ **Automated data pipeline** using Apache Airflow
- 🐦 **Real-time tweet extraction** from Twitter API using Tweepy
- 🧹 **Data transformation** into clean, structured format
- ☁️ **Secure upload to Amazon S3**
- 🔁 Supports **scheduling, retries**, and **logging** via Airflow

---

## 📊 ETL Workflow Overview

1. **Extract**: Connects to Twitter API using Tweepy to fetch recent tweets from a specified user (e.g., `@elonmusk`).
2. **Transform**: Filters relevant fields (text, created_at, likes, retweets), formats datetime, and removes duplicates.
3. **Load**: Saves the transformed data as a CSV and uploads it directly to an **Amazon S3** bucket.

---

## 🛠️ Tech Stack

| Tool         | Purpose                         |
|--------------|----------------------------------|
| **Apache Airflow** | DAG orchestration and scheduling |
| **Tweepy**         | Twitter API integration         |
| **Pandas**         | Data manipulation & transformation |
| **AWS S3**         | Cloud data storage              |
| **Python**         | Core programming language       |

---


## ⚙️ How to Run
Create an EC2 instance. In this project I used an Ubantu t3.medium EC2 instance. 
SSH into your EC2 instance. 

## Run following commands to install required applications in EC2 instance: 
sudo apt-get update
sudo apt install python3-pip
sudo apt install python3-venv -y
python3 -m venv airflow_venv
source airflow_venv/bin/activate
pip install --upgrade pip
pip install apache-airflow pandas s3fs tweepy

## Run airflow server using
airflow standalone

## Make sure your EC2 instance has enough security rules to run the airflow on localhost. You can modify these security rules from Security Groups of your instance

## Login to Airflow
## Create an S3 bucket 
## Upload your files to your instance to run on Airflow
## Check if your DAG is now listed in Airflow 
## Run the DAG
## Go to your AWS account and check if the data has been uploaded to S3 bucket



## 📦 Sample Output

The transformed CSV is automatically uploaded to:
```
s3://your-bucket-name/twitter_data/elonmusk_tweets.csv
```

---



## 👨‍💻 Author

**Divyansh Soni**  
🟦 [LinkedIn](https://www.linkedin.com/in/divyansh-prakhar-soni-95b255152/) 


---
