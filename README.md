# DoneDeal-Data-Scraping
DoneDeal website data scraping using python

1. Getting data from DoneDeal (WebScraping using python) (webscrapingpython.py)
2. Hosted in AWS EC2 Instance (as I dont want to mess up my local storage)
3. Initally stored data in S3 but due to limited requests in free trial had to store in ebs volumne within AWS.
4. Was looking out for different ways to run my python program in the background - the 2 best solutions that I could find was tmux and docker.
5. Already used Docker so wanted to try tmux.
6. Using tmux - python program keeps running in the background even when my pc is off ( The csv file keeps updating after every interval)
7. From local terminal ssh into ec2 instance to bring over the csv file and do some transformations/ cleaning so that it be used for further visualaizations and predicitons
8. SCP command to securely transfer files between local and remote host
9. Data Cleaning within Jupyter notebook (Data Cleaning.ipyb)
10. Data Visualizations (DoneDeal Visualizations.ipynb) (More to be added soon)
11. Using SQLite or Pandas (which provides an interface to SQLite) in Python querying CSV file using SQL (Added feature to run sql queries) (SQLQueryRunOnCSV.py)
12. Predictions:
    1. Car Price Fluctuation Analysis: Using time-series analysis to investigate the price fluctuations of cars from different brands over time. Separate time-            series plots for each car brand, showing how the average price of cars from that brand fluctuates over time. By examining these plots, you can gain insights        into the price trends and fluctuations for different car brands. (Car Price Fluctuation Analysis.ipynb)
   
    2. Popular Car brands: A simple analysis to find the most popular car brands, which can be achieved through basic data manipulation and aggregation.(Popular            car brands.ipynb)
       
    3. Car Mileage Prediction: 

14. Now working on predictions using ML Algos........


    More features to be added soon:-
    - Predictions
    - host website on local: for ex- "Sell any car - Price Avg" etcccc
    - Creating an API
    - and many more... :)
   
* Many improvements can still be done I know within all the python codes, I am just learning at this time and keeping aside the fact about run- time, clean codes 
* I will work on simplifying and cleaning up my code for better performace in the coming days alongside adding new features 
