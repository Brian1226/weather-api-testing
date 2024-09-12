# Weather API Testing

This project involves testing the Current Weather Data API provided by [OpenWeather](https://openweathermap.org/current). It uses the Requests library to send a GET request to the API and leverages pytest for unit testing. Testings include mocking to simulate API responses and validating the functionality of the function under test, and ensuring proper error handling.

## Project Structure

- `src/app.py`: Contains the implementation of the `get_coordinates` and `get_weather_data` function using the API.
- `tests/test_app.py`: Contains the test cases for verifying the functionality of the functions.

## Installation
1. Get a free API key by creating an account at https://home.openweathermap.org/users/sign_up
2. Clone the repository
   ```bash
   git clone https://github.com/Brian1226/weather-api-testing.git
   ```
3. Install these dependencies
   ```bash
   pip install requests python-dotenv pytest
   ```
4. Create a `.env` file in the root directory and enter your API key
   ```bash
   API_KEY = your_api_key_here
   ```

## Usage
- To run the application and generate coordinates and current weather & temperature, use `python src/app.py`
- To run the tests, use `python -m pytest`

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
