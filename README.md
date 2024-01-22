# ML_Zoomcamp_capstone2

## Taxi fare prediction

Download the database from here:
https://www.kaggle.com/datasets/raviiloveyou/predict-taxi-fare-with-a-bigquery-ml-forecasting?resource=download

It comes in 2 separate dataset, one for train and another for test.
I used the train dataset for this project.

There are 8 features:
- 'trip_duration': How long did the journey last?[in Seconds]

- 'distance_traveled': How far did the taxi travel?[in Km]

- 'num_of_passengers': How many passengers were in the taxi?

- 'fare': What's the base fare for the journey?(this is your prediction target!)[In INR]

- 'tip': How much did the driver receive in tips?[In INR]

- 'miscellaneous_fees': Were there any additional charges during the trip?e.g. tolls, convenience fees, GST
etc.[In INR]

- 'total_fare': The grand total for the ride. It's the sum of fare, tip, and miscellaneous_fees[In INR]

- 'surge_applied': Was there a surge pricing applied? Yes or no?

Target variable: fare

The objective is to predict the taxi's fare.
And for that, I used 3 ML algorithms: linear regression, random forest, decision tree

The file's description below:

Notebook.ipynb - Data preparation / EDA and feature importance analysis / Model Selection procedure and parameter tunning

train.py - Training the final model / Saving it to a file using pickle

predict.py - Loading the model / Serving it via Flask or waitress or gunicorn

testing-predict.py - run it to test the service that should be running with docker, flask, waitress or gunicorn

Pipfile, pipfile.lock - files with dependencies needed to run the project

Dockerfile - contains the image to be downloaded from docker hub, the commands to run, and files to be copied.

#### Deploying with waitress:

- Download the files: Pipfile, pipfile.lock, model_rf.bin, predict.py, testing_predict.py
- Run the following in Powershell/Command Prompt/Gitbash: pipenv run waitress-serve --listen=0.0.0.0:9696 predict:app
- Run the testing-predict.py file in another window of Powershell/Command Prompt/Gitbash

#### Deploying with Docker:

- Make sure the docker is running.
- Have the following files in the same folder: Dockerfile, Pipfile, pipfile.lock, model_rf.bin, predict.py, testing_predict.py
- Create an image based on Dockerfile on Powershell or Command Prompt or Gitbash: docker build -t zoomcamp-capstone2 .
- Run the image just created: docker run -it --rm -p 9696:9696 zoomcamp-capstone2
- Run the testing-predict.py file in another window of Powershell/Command Prompt/Gitbash
