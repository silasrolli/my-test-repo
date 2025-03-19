class WGS84Coord:
    def __init__(self, longitude=0, latitude=0):
        self.longitude = longitude
        self.latitude = latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value < -180:
            print("Warnung: Longitude unter -180, auf -180 gesetzt.")
            self._longitude = -180
        elif value > 180:
            print("Warnung: Longitude über 180, auf 180 gesetzt.")
            self._longitude = 180
        else:
            self._longitude = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value < -90:
            print("Warnung: Latitude unter -90, auf -90 gesetzt.")
            self._latitude = -90
        elif value > 90:
            print("Warnung: Latitude über 90, auf 90 gesetzt.")
            self._latitude = 90
        else:
            self._latitude = value

coord1 = WGS84Coord(200, 100)
print(f"Koordinate 1: Longitude = {coord1.longitude}, Latitude = {coord1.latitude}")

coord2 = WGS84Coord(-75, 45)
print(f"Koordinate 2: Longitude = {coord2.longitude}, Latitude = {coord2.latitude}")

coord3 = WGS84Coord(-190, -95)
print(f"Koordinate 3: Longitude = {coord3.longitude}, Latitude = {coord3.latitude}")
