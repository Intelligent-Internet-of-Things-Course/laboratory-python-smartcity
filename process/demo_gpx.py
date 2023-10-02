from resources.gpx_gps_resource import GpxGeoLocation
from model.geo_location import GeoLocation
from time import sleep

target_gpx_file = "../tracks/mantova_demo_track.gpx"
gpx_geo_location = GpxGeoLocation(target_gpx_file)

# Test reference GeoLocation to evaluate the distance while iterating over the gpx locations
test_geo_location = GeoLocation(45.155630602701514, 10.788790591249956, 0.0)

while True:

    # Update the location measurement
    updated_loc = gpx_geo_location.update_measurements()

    print(f'Updated GeoLoc: Lat: {updated_loc.latitude} - Lng: {updated_loc.longitude} - Ele: {updated_loc.elevation}')

    # Compute the distance between the
    geo_distance_km = GeoLocation.distance(
        (updated_loc.latitude, updated_loc.longitude),
        (test_geo_location.latitude, test_geo_location.longitude)
    )

    print(f'Distance with Test GeoLoc: {geo_distance_km}')

    sleep(1)