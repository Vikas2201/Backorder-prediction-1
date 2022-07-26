# Backorder-prediction
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem Statement
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Backorders are unavoidable, but by anticipating which things will be backordered, planning can be streamlined at several levels, preventing unexpected strain on production, logistics, and transportation. ERP systems generate a lot of data (mainly structured) and also contain a lot of historical data; if this data can be properly utilized, a predictive model to forecast backorders and plan accordingly can be constructed. Based on past data from inventories, supply chain, and sales, classify the products as going into backorder (Yes or No).

# Data Analysis
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the Train dataset we are provided with 23 columns(Features) of data.

* Sku(Stock Keeping unit) : The product id — Unique for each row so can be ignored
* National_inv : The present inventory level of the product
* Lead_time : Transit time of the product
* In_transit_qty : The amount of product in transit
* Forecast_3_month , Forecast_6_month , Forecast_9_month : Forecast of the sales of the product for coming 3 , 6 and 9 months respectively
* Sales_1_month , sales_3_month ,sales_6_month , sales_9_month : Actual sales of the product in last 1 , 3 ,6 and 9 months respectively
* Min_bank : Minimum amount of stock recommended
* Potential_issue : Any problem identified in the product/part
* Pieces_past_due: Amount of parts of the product overdue if any
* Perf_6_month_avg , perf_12_month_avg : Product performance over past 6 and 12 months respectively
* Local_bo_qty : Amount of stock overdue
* Deck_risk , oe_constraint, ppap_risk, stop_auto_buy, rev_stop : Different Flags (Yes or No) set for the product
* Went_on_backorder : Target variable

Out of the 23 features given in the dataset 15 are numerical and 8(including the target variable) are categorical features.

# Approach
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The main goal is to predict the whether a product comes in backorder or not based on different factors available in the dataset.

* Data Exploration : Exploring dataset using pandas,numpy,matplotlib and seaborn.
* Data visualization : Ploted graphs to get insights about dependend and independed variables.
* Feature Engineering : Removed missing values and created new features as per insights.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Model Selection II : Performed Hyperparameter tuning using RandomsearchCV.
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on AWS .

# Technologies Used
-------------------------------------------------------------------------------------------------------------------------------------------------------------

 * Pycharm Is Used For IDE.
 * For Visualization Of The Plots Matplotlib , Seaborn Are Used.
 * AWS is Used For Model Deployment.
 * Cassandra Database Is Used To As Data Base.
 * Front End Deployment Is Done Using HTML , CSS.
 * Flask is for creating the application server and pages.
 * Git Hub Is Used As A Version Control System.
 * josn is for data validation processes.
 * os is used for creating and deleting folders.
 * csv is used for creating .csv format file.
 * numpy is for arrays computations and mathematical operations
 * pandas is for Manipulation and wrangling structured data
 * scikit-learn is used for machine learning tool kit
 * pickle is used for saving model
 * XgBoost is used for XgBoostClassifier Implementation.
 * Nearmiss Imbalance is used for handling Imbalance Data.

# User InterFace 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Home Page 

<p align="center">
  <img src="https://user-images.githubusercontent.com/76476273/132872549-65c3ee52-5160-4ceb-ab06-4ed8940d9910.png" width='600px'>
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/76476273/132872622-e02ff9bb-b2e6-458f-a74b-ce02cb448d76.png" width='600px'>
</p>

* Predict Page

<p align="center">
  <img src="https://user-images.githubusercontent.com/76476273/132872651-805d24e3-5e38-46a5-b10a-631ab59b888c.png" width='600px'>
</p>


# Back Order Prediction Project Video 
-----------------------------------------------------------------------------------------------------------------------------------------------------


https://user-images.githubusercontent.com/76476273/132907109-6652c535-4921-4451-87cc-cfe353b2a3cb.mp4


# Deployment Links
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 AWS link : http://ec2-18-133-246-122.eu-west-2.compute.amazonaws.com:8080
 
 # Develoyment Process Video
 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
https://user-images.githubusercontent.com/76476273/132998251-d9c7e580-f0d4-4260-9145-250d8b8ad212.mp4


 
 # Run Locally
 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* Clone the project
```bash
  git clone https://github.com/Vikas2201/Backorder-prediction-1
```
* Go to the project directory
```bash
  cd Backorder-prediction-1
 ```
* Install dependencies
```bash
  pip install -r requirements.txt
```
* Setting up the Controllers files
```bash
    Update the values inside the Controllers folder
```
* Run the app.py
```bash
  python app.py
```

# Usage
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In Development If You Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

* Fork the repo

* Create a new branch
```bash
   git checkout -b new-feature
```
* Make the appropriate changes in the file

* Commit your changes
```bash
     git commit -am "New feature added"
```
* Push to the branch
```bash
      git push origin new-feature
```
* Create a pull request

# Directory Tree

```bash
└── Backorder-Prediction
    ├── application_logging
    │   └── logging.py        
    ├── Controllers
    │   └── DBconnection_info.yaml
    ├── Data_Information 
    │   └── Null_Values.csv
    ├── data_ingestion
    │   ├── __pycache__
    │   └── data_loader.py
    ├── data_preprocessing
    │   ├── __pycache__
    │   └── preprocessing.py
    ├── EDA 
    │   ├── EDA-part1.ipynb
    │   └── EDA-part2.ipynb
    ├── model 
    │   └── Random Forest
    │       └── Random Forest.sav 
    ├── model_finder
    │   ├── __pycache__
    │   └── Model.py
    ├── Prediction_logs 
    │   └── predictionlog.txt 
    ├── Prediction_Output_File 
    │   └── Predictions.csv 
    ├── ReplaceMissingwithNull
    │   ├── __pycache__
    │   ├── __init__.py
    │   └── transformer.py
    ├── Save_Models
    │   ├── __pycache__
    │   └── save_methods.py
    ├── static 
    │   ├── backorder.jpg
    │   ├── Style1.css
    │   └── Style2.css 
    ├── Templates
    │   ├── index.html 
    │   └── predict.html 
    ├── Tools
    │   ├── __pycache__
    │   ├── __init__.py
    │   ├── DBconnector.py
    │   ├── training_logFilescreater.py
    │   └── YamlParser.py
    ├── Traning_batch_Files
    │   └── BackOrder_08012020_120000.csv
    ├── Training_Database_operations 
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── Database_handler.py
    ├── Traininig_dataValidation 
    │   ├── __pycache__
    │   └── RawtrainingValidation.py 
    ├── Training_FilesfromDB
    │   └── InputFile.csv 
    ├── Training_Logs
    │   ├── columnValidationLog.txt
    │   ├── DataBaseConnectionLog.txt
    │   ├── Datapreprocessing_logs.txt
    │   ├── GeneralLog.txt
    │   ├── TmissingValuesInColumn.txt
    │   ├── ModelTrainingLog.txt
    │   ├── nameValidationLog.txt
    │   ├── TrainingDatabseInfo.txt
    │   ├── TrainingMainLog.txt
    │   ├── valuesfromSchemaValidationLog.txt
    │   └── yaml_parser.txt
    ├── Training_Raw_Files_Validated
    │   └── BackOrder_08012020_120000.csv
    ├── training_val_linkage.py
    ├── training_file.py
    ├── app.py
    ├── prediction.py
    ├── requierements.txt 
    ├── Training_Schema.json
    └── secure-connect-backorder-prediction.zip
  ```
  
 # Conclusions
 -------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
We Developed A Product Backorder Predictive Model With The Capability Of Identifying Items To Be Backordered Using Machine Learning Models. The Proposed Approach Accept Input Data Was Pre-Processed By Way Of Missing Values Imputation, Non-Numeric To Numeric Feature Conversion And Normalization, And Split Into Training And Test Set. The Training Set Is Passed Into A Data Balancing Module To Ensure Equal Class Distribution And Avoid Biasness In Learning Model Decisions. The Imbalanced Training Data Were Subjected Sampling As We Concurrently Fed The Data Into Sampling Techniques Fed Into ML Models To Predict Product Backorders. The Predictive Models Were Validated On Test Data And Their Performances Were Evaluated. The Evaluation Of The Result Obtained Showed By Precision, Recall , AUC Score , Accuracy And F1-Score.


# Teams Members Name
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 * [@Vikas](https://github.com/Vikas2201)
 * [@Chaudhary Shubham R.](https://github.com/shubhamchau222)
 * [@Bijayalaxmi Kar](https://github.com/bijayalaxmikar)
 * [@Hitesh Singh](https://github.com/hitesh777)
 * [@Pallapothu Bhargavram](https://github.com/bhargavtejasw)
 * [@Vivek Rathore](https://github.com/VIVEKRATHORE360)

# Help Me Improve
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Hello Reader if you find any bug please consider raising issue I will address them asap.

# Documentation
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[High Level Documentation](https://github.com/Vikas2201/Backorder-prediction-1/files/7145911/Backorder.HLD.V1.0.pdf)

[Low Level Documentation](https://github.com/Vikas2201/Backorder-prediction-1/files/7145912/Low.Level.Document.pdf)

[WireFrame](https://github.com/Vikas2201/Backorder-prediction-1/files/7144748/WireFrame_By_Vikas.pdf)

[Detail Project Report](https://github.com/Vikas2201/Backorder-prediction-1/files/7145926/DPR.pdf)

[Architecture Documentation](https://github.com/Vikas2201/Backorder-prediction-1/files/7145934/Architecture.pdf)

