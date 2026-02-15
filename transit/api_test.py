import http.client
from dotenv import load_dotenv
import os

# load env variables
load_dotenv()

# define env variables
TRANSIT_SECRET = os.getenv("TRANSIT_SECRET")
LAT = os.getenv("LAT")
LON = os.getenv("LON")

conn = http.client.HTTPSConnection("external.transitapp.com")

headers = { 'apiKey': TRANSIT_SECRET or "" }

parameters = f"?lat={LAT}&lon={LON}"

conn.request("GET", f"/v3/public/nearby_routes{parameters}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))