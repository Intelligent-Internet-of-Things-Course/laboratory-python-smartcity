import json
import gpxpy
import gpxpy.gpx
from model.geo_location import GeoLocation


class GpxGeoLocation:

    def __init__(self, gpx_file_path):
        self.gpx_file_path = gpx_file_path
        self.tracks = None
        self.waypoints = None
        self.__init_track()
        self.current_location = None
        self.current_index = 0
        self.is_reverse = False

    def __init_track(self):

        print(f'Loading GPX Track: {self.gpx_file_path}')

        try:
            gpx_file = open(self.gpx_file_path, 'r')
            gpx = gpxpy.parse(gpx_file)
            self.tracks = gpx.tracks
            self.waypoints = gpx.waypoints

            print(f'{len(self.waypoints)} Correctly Loaded !')

        except Exception as err:
            print(f'Error reading target GPX File: {err}')

    def update_measurements(self):

        current_waypoint = self.waypoints[self.current_index]

        self.current_location = GeoLocation(current_waypoint.latitude,
                                            current_waypoint.longitude,
                                            current_waypoint.elevation)

        #print(f'Current Index: {self.current_index} - GeoLocation: {self.current_location}')

        if self.is_reverse is False and self.current_index < len(self.waypoints) - 1:
            self.current_index = self.current_index + 1
        elif self.is_reverse is False and self.current_index == len(self.waypoints) - 1:
            self.is_reverse = True
            self.current_index = self.current_index - 1
        elif self.is_reverse is True and self.current_index > 0:
            self.current_index = self.current_index - 1
        elif self.is_reverse is True and  self.current_index == 0:
            self.is_reverse = False
            self.current_index = self.current_index + 1

        return self.current_location

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
