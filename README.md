# DoneDeal-Data-Scraping
DoneDeal website data scraping using python

1. Getting data from DoneDeal (WebScraping using python) (webscrapingpython.py)
2. Hosted in AWS EC2 Instance (as I dont want to mess up my local storage)
3. Initally stored data in S3 but due to limited requests in free trial had to store in ebs volumne within AWS.
4. Was looking out for different ways to run my python program in the background - the 2 best solutions that I could find was tmux and docker.
5. Already used Docker so wanted to try tmux.
6. Using tmux - python program keeps running in the background even when my pc is off ( The csv file keeps updating after every interval )
7. From local terminal ssh into ec2 instance to bring over the csv file and do some transformations/ cleaning so that it be used for further visualaizations and predicitons
8. SCP command to securely transfer files between local and remote host
9. Data Cleaning within Jupyter notebook (Data Cleaning.ipyb)
10. Data Visualizations (DoneDeal Visualizations.ipynb) (More to be added soon)
11. Now working on predictions using ML Algos........


    More features to be added soon:-
    - Predictions
    - host website on local: for ex- "Sell any car - Price Avg" etcccc
    - Creating an API
    - and many more... :)
   
* Many improvements can still be done I know within all the python codes, I am just learning at this time and keeping aside the fact about run- time, clean codes 
* I will work on simplifying and cleaning up my code for better performace in the coming days alongside adding new features 
