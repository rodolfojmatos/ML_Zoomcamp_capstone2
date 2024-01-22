import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
customer = {
    'trip_duration':134.0,
    'distance_traveled':1.48,
    'num_of_passengers':1.0,
    'tip':0,
    'miscellaneous_fees':6.0,
    'surge_applied':0,
}

response = requests.post(url, json=customer).json()
print(response)

print('Calculated Fare=%.3f' % (response['fare_probability']))
print('Real Fare= 33.75')
