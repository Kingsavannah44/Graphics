import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

from opencage.geocoder import OpenCageGeocode

import folium


key = "79665ce9e4c8427ca397cec47b6dd18a"


check_number = phonenumbers.parse("+254715970249")
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)


phoneNumber = phonenumbers.parse("+254715970249") 
print(carrier.name_for_number(check_number, "en"))

geocoder = OpenCageGeocode(key)

querry = str(number_location)
results = geocoder.geocode(querry)



lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)


map_location =folium.Map(location = [lat,lng],zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")

 