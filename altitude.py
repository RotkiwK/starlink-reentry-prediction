import math

MU = 398600.4418          # Earth's gravitational parameter, km^3/s^2
EARTH_RADIUS_KM = 6378.137  # Earth's equatorial radius, km


def altitude_from_mean_motion(mean_motion):
    # convert mean motion from revolutions per day to radians per second
    n_rad_per_s = (mean_motion * 2 * math.pi) / 86400
    orbit_radius = (MU / (n_rad_per_s ** 2)) ** (1 / 3)
    altitude = orbit_radius - EARTH_RADIUS_KM
    return altitude


print(altitude_from_mean_motion(15.5))
print(altitude_from_mean_motion(16))
print(altitude_from_mean_motion(15.06))