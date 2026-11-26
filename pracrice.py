import math

MU = 398600.4418          # Earth's gravitational parameter, km^3/s^2
EARTH_RADIUS_KM = 6378.137  # Earth's equatorial radius, km


def altitude_from_mean_motion(mean_motion):
    # convert mean motion from revolutions per day to radians per second
    n_rad_per_s = (mean_motion * 2 * math.pi) / 86400
    orbit_radius = (MU / (n_rad_per_s ** 2)) ** (1 / 3)
    altitude = orbit_radius - EARTH_RADIUS_KM
    return altitude


tles = [
    {"EPOCH": "2024-03-01", "MEAN_MOTION": 15.5},
    {"EPOCH": "2024-03-15", "MEAN_MOTION": 15.7},
    {"EPOCH": "2024-03-29", "MEAN_MOTION": 15.9},
]

for tle in tles:
    tle["ALTITUDE_KM"] = altitude_from_mean_motion(tle["MEAN_MOTION"])
    print(tle["EPOCH"], round(tle["ALTITUDE_KM"], 1))
    