# Geocoder

This is a geocoding service that caches and fetches results from the Google and HERE geocoding services.  It is implemented
as a WSGI app.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Geocoder was built and tested with Python 2.7.10.  For the best compatibility, please use Python 2.7.10

### Installing

First set up virtualenv for the project to isolate your python environment.  From the cloned repository root...

```
virtualenv .venv
source .venv/bin/activate
```

The following python modules are required and can be installed via pip.

```
pip install falcon
pip install requests
```

Since this is a WSGI app, the gunicorn WSGI server is recommended for running the app.  This works great for MacOS.  Explore Waitress if you are on Windows instead of gunicorn.

```
pip install gunicorn
```

### Running locally

There are a few environment variables that this app requires since it depends on the Google and HERE apis.

The environment variables that must be set are:
API_KEY_GOOGLE_GEOCODING
API_HERE_APP_CODE
API_HERE_APP_ID

They will be supplied after you request the appropriate API access from Google and HERE for their geocoding APIs.

These environment variables can either be set directly or inline with launching the app under gunicorn as demonstrated below in a MacOS terminal

```
API_KEY_GOOGLE_GEOCODING=YOUR_DATA_HERE API_HERE_APP_CODE=YOUR_DATA_HERE API_HERE_APP_ID=YOUR_DATA_HERE gunicorn geocoder.app
```

For ease of development, we recommend using the --reload flag to gunicorn so that it will automatically load any changes that you make

 ```
API_KEY_GOOGLE_GEOCODING=YOUR_DATA_HERE API_HERE_APP_CODE=YOUR_DATA_HERE API_HERE_APP_ID=YOUR_DATA_HERE gunicorn --reload geocoder.app
```

### Available routes, Sample usage

After the service is started, the following routes are available

GET /v1/geocode/json - address is a required query parameter in which an encoded address is supplied.

For example: GET /v1/geocode/json?address=425+Market+St,+San+Francisco,+CA+94105

will return a response like
```
{
    "address": "425 Market St+ San Francisco+ CA 94105", 
    "lat": 37.79119130000001, 
    "lng": -122.3983658
}
```

Be aware that by default, gunicorn initializes the WSGI server to listen on port 8000.

## Built With

* [Falcon](https://falconframework.org/) - The web API framework used 
* [Google Geocoding Service](https://developers.google.com/maps/documentation/geocoding/start)
* [HERE Geocoding Service](https://developer.here.com/documentation/geocoder/topics/quick-start.html)

## Authors

* **Anthony Chen** - *Initial work* - [antmit](https://github.com/antmit)
