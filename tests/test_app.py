import pytest
import unittest.mock as mock
import requests
import src.app as app


@pytest.fixture
def mock_get():
    with mock.patch("src.app.requests.get") as mock_get:                               # fixture that replaces 'requests.get' with 'mock_get'
        yield mock_get


@pytest.mark.parametrize(                                                              # sets of inputs to check for expected latitude and longitude
        'city, state, country, expected_lat, expected_lon',
        [
            ('San Jose', 'California', 'US', 37.3361663, -121.890591),
            ('Buffalo', 'New York', 'US', 42.8867166, -78.8783922),
            ('Chicago', 'Illinois', 'US', 41.8755616, -87.6244212),

        ]
)


def test_get_coordinates(city, state, country, expected_lat, expected_lon, mock_get):
    mock_get.return_value.status_code = requests.codes.ok                               # simulates successful HTTP response
    mock_get.return_value.json.return_value = [                                         # simulates JSON payload returned by API
        {
            'lat': expected_lat,
            'lon': expected_lon,
        }
    ]
    lat, lon = app.get_coordinates(city, state, country)                                # calls the function to be tested
    assert lat == expected_lat                                                          # asserts that the return value is correct
    assert lon == expected_lon


@pytest.mark.parametrize(                                                               # sets of inputs to check for expected weather
        'lat, lon, expected_weather',
        [
            (37.3361663, -121.890591, 'clear sky'),
            (42.8867166, -78.8783922, 'smoke'),
            (41.8755616, -87.6244212, 'scattered clouds'),
        ]
)


def test_get_weather_data(lat, lon, expected_weather, mock_get):
    mock_get.return_value.status_code = requests.codes.ok
    mock_get.return_value.json.return_value = {
        'weather': [
            {
                'description': expected_weather,
            }
        ],
    }
    weather_data = app.get_weather_data(lat, lon)
    assert weather_data["weather"][0]["description"] == expected_weather


@pytest.mark.parametrize(                                                               # test different values of city, state, country 
        'city, state, country',
        [
            ('San Jose', 'California', 'US'),
            ('Buffalo', 'New York', 'US'),
            ('Chicago', 'Illinois', 'US'),

        ]
)


def test_get_coordinates_error(city, state, country, mock_get):
    mock_get.return_value.status_code = requests.codes.bad_request                       # simulates unsuccessful HTTP response                   
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError   # simulates raise_for_status() to raise an HTTPError
    with pytest.raises(requests.exceptions.HTTPError):                                   # asserts that the function raises an HTTPError
        app.get_coordinates(city, state, country)                                        # raise_for_status() raises error, so triggers pytest.raises assertion


@pytest.mark.parametrize(                                                               # test different values for latitude and longitude
        'lat, lon',
        [
            (37.3361663, -121.890591),
            (42.8867166, -78.8783922),
            (41.8755616, -87.6244212),
        ]
)


def test_get_weather_data_error(lat, lon, mock_get):
    mock_get.return_value.status_code = requests.codes.bad_request
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError
    with pytest.raises(requests.exceptions.HTTPError):
        app.get_weather_data(lat, lon)
