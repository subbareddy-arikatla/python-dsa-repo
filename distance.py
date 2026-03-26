import math

def haversine(lat1, lon1, lat2, lon2):
    # Earth radius in kilometers
    R = 6371  

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + \
        math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.asin(math.sqrt(a))

    return R * c

# Example
print(haversine(12.9716, 77.5946, 28.7041, 77.1025))  # Bangalore → Delhi
