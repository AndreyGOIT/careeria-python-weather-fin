Precision Weather – Python Project

A Python command-line application that stores user-selected cities, fetches current temperature data from the Finnish Meteorological Institute (FMI) Open Data API, and logs successful and failed weather queries.

This project was developed as part of the Careeria Python Training Course.

⸻

🚀 Features

1. City Management

When the program starts, it asks:

Do you want to modify the list of tracked cities? (K = yes)

    •	If the user enters K, the program:
    •	clears the paikkakunnat table
    •	prompts for new city names in a loop
    •	stops when X is entered
    •	Otherwise, previously saved cities are used

2. Data Storage (SQLite)

The project uses a local SQLite database:

data.db
└── paikkakunnat (id, name)

All SQL operations are handled via db_utils.py.

⸻

🌡 Fetching Temperature from FMI Open Data

Weather data is retrieved using the fmiopendata library via the stored query:

fmi::observations::weather::multipointcoverage

The script extracts the latest available temperature value for each city.

⸻

📝 Logging

All events are recorded in:

lokitiedosto.txt

The log includes:
• timestamp
• successful temperature queries
• city names that produced errors
• updates to the city list

The log file is not overwritten, only appended.

⸻

📂 Project Structure

careeria-python-weather-fin/
│
├── main.py # main program flow
├── db_utils.py # database helpers
├── weather_fetcher.py # API requests and parsing
├── lokitiedosto.txt # log file
├── data.db # SQLite database
├── test_weather.py # standalone weather test
└── README.md

⸻

🔧 Installation

Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install fmiopendata requests

⸻

▶️ Running the Application

python3 main.py

⸻

🧪 Testing Weather Fetching

python3 test_weather.py

Expected output example:

3.9
2.8
0.0

⸻

📌 Example Program Output

Haluan muuttaa seurattavia paikkakuntia? (K = kyllä, muuta = ei)
Paikkakuntia ei muutettu.
['Helsinki', 'Porvoo', 'Turku']

Haetaan lämpötilat...

Helsinki 3.9 °C
Porvoo 2.8 °C
Turku 0.0 °C

Lämpötilahaut suoritettu. Haettu onnistuneesti: 3 paikkakuntaa.

⸻
