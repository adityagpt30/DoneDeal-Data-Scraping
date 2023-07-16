#!/usr/bin/env python
# coding: utf-8

import requests
import time
import csv
# import boto3  # Commented out since S3 functionality is not required
from bs4 import BeautifulSoup

# ACCESS_KEY = 'your_access_key'
# SECRET_KEY = 'your_secret_key'
# BUCKET_NAME = 'your_bucket_name'

def find_cars():
    html_text = requests.get('https://www.donedeal.ie/cars').text
    soup = BeautifulSoup(html_text, 'lxml')
    cars = soup.find_all('li', class_='Listings__Mobile-sc-1igquny-2 dfcoGb')

    # s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

    for car in cars:
        title = car.find('p', class_='Card__Title-sc-1v41pi0-4 duHUaw').text
        price = car.find('p', class_='Card__InfoText-sc-1v41pi0-13 jDzR').text
        year = car.find('li', class_='Card__KeyInfoItem-sc-1v41pi0-5 hGnmwg ki-1').text
        engine = car.find('li', class_='Card__KeyInfoItem-sc-1v41pi0-5 hGnmwg ki-2').text
        miles = car.find('li', class_='Card__KeyInfoItem-sc-1v41pi0-5 hGnmwg ki-3').text
        day_posted_element = car.find('li', class_='Card__KeyInfoItem-sc-1v41pi0-5 hGnmwg ki-4')

        if day_posted_element:
            day_posted = day_posted_element.text
        else:
            day_posted = ''

        header = ['Car Name', 'Price', 'Year', 'Engine', 'Mileage', 'Day Posted']
        data = [title, price, year, engine, '', '']

        with open('DoneDealCars.csv', 'r', newline='', encoding='UTF8') as f:
            reader = csv.reader(f)
            existing_cars = [row[0] for row in reader]

        if title not in existing_cars and miles not in existing_cars:

            dayposted_keywords = ['hour', 'hours', 'min', 'mins', 'day', 'days']  # mileage keywords here

            if any(keyword in day_posted for keyword in dayposted_keywords):
                data[5] = day_posted  # Assign value to 'Day Posted' column

            if any(keyword in miles for keyword in dayposted_keywords):
                data[5] = miles  # Assign value to 'Day Posted' column
            else:
                data[4] = miles  # Assign value to 'Mileage' column

            with open('DoneDealCars.csv', 'a+', newline='', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(data)

            # Upload the CSV file to S3 bucket
            # s3.upload_file('DoneDealCars2.csv', BUCKET_NAME, 'DoneDealCars2.csv')

if __name__ == '__main__':
    while True:
        find_cars()
        time.sleep(10)
        
