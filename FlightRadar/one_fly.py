
from FlightRadar24 import FlightRadar24API
fr_api = FlightRadar24API()

airlines = fr_api.get_airlines()
flights = fr_api.get_flights()  # Returns a list of Flight objects

print(flights[0])

