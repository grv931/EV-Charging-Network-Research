import math

def haversine(coord1, coord2):
    """
    Compute the great-circle distance between two (latitude, longitude) pairs.
    Coordinates must be given in decimal degrees.
    Returns the distance in kilometers.
    """
    r_earth = 6371.0  # Earth radius in km
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return r_earth * c


def total_distance(site_list, coords):
    """
    For a list of site names, sum the Haversine distances for every unique pair.
    coords is a dictionary mapping site->(lat,lon).
    """
    n = len(site_list)
    total = 0.0
    for i in range(n - 1):
        for j in range(i + 1, n):
            total += haversine(coords[site_list[i]], coords[site_list[j]])
    return total


# Five PSO-generated combinations from the provided output (33 stations each)
top_combinations = [
    # Combination 1 (Fitness 0.6598)
    ['Saheed Nagar', 'Charger – Geetanjali', 'Tata Power – BMC Bhawani Mall', 'Tata Power – Dion Automotives', 
     'HPCL – Regional Office', 'Palasuni', 'Sishu Bhawan', 'Tata Power – DN Group Corporate', 'Vani Vihar', 
     'Tata Power – MG Bhubaneswar', 'Tata Power – Regalia Mall (DN Square)', 'Kazam – Rasulgarh', 
     'Tata Power – CSM Technologies', 'Statiq – Yellowings ITC Cuttack Station', 'Tata Power – DN Wisdom Tree', 
     'Tata Power – GUGNANI TYRES', 'Jagamara', 'Tata Power – Audi Bhubaneswar', 'Jaydev Vihar', 'Tankapani Road', 
     'Tata Power – MLCP Saheed Nagar', 'Pokhariput', 'KIIT', 'Nayapalli', 'GLIDA DLF Bhubaneswar – Statiq', 
     'Statiq – Nexus Esplanade Mall', 'Kalinga Stadium', 'Mancheswar', 'Chandrasekharpur', 'Satya Nagar', 
     'TML Tirupati Enterprises', 'Badagada', 'Tata Power – GUGNANI AUTOCARS'],
    # Combination 2 (Fitness 0.6486)
    ['Tata Power – BMC Bhawani Mall', 'Vani Vihar', 'Saheed Nagar', 'Nayapalli', 
     'Statiq – Yellowings ITC Cuttack Station', 'Tata Power – DN Group Corporate', 'Kazam – Rasulgarh', 
     'Charger – Geetanjali', 'KIIT', 'Jagamara', 'Tata Power – Regalia Mall (DN Square)', 
     'Tata Power – MLCP Saheed Nagar', 'Kalinga Stadium', 'GLIDA DLF Bhubaneswar – Statiq', 'Jaydev Vihar', 
     'Tata Power – MG Bhubaneswar', 'Tata Power – CSM Technologies', 'TML Tirupati Enterprises', 'Tankapani Road', 
     'Tata Power – GUGNANI TYRES', 'Sishu Bhawan', 'HPCL – Regional Office', 'Tata Power – Audi Bhubaneswar', 
     'Pokhariput', 'Tata Power – Dion Automotives', 'Palasuni', 'Tata Power – DN Wisdom Tree', 
     'Statiq – Nexus Esplanade Mall', 'Badagada', 'Mancheswar', 'Satya Nagar', 'Tata Power – GUGNANI AUTOCARS', 
     'Chandrasekharpur'],
    # Combination 3 (Fitness 0.6480)
    ['Saheed Nagar', 'Nayapalli', 'Statiq – Nexus Esplanade Mall', 'Tata Power – BMC Bhawani Mall', 
     'Tata Power – Audi Bhubaneswar', 'Jagamara', 'Vani Vihar', 'Statiq – Yellowings ITC Cuttack Station', 
     'Tata Power – Regalia Mall (DN Square)', 'Charger – Geetanjali', 'Tankapani Road', 
     'Tata Power – Dion Automotives', 'Sishu Bhawan', 'Chandrasekharpur', 'Badagada', 'Kazam – Rasulgarh', 
     'HPCL – Regional Office', 'Tata Power – CSM Technologies', 'Pokhariput', 'Tata Power – MLCP Saheed Nagar', 
     'Kalinga Stadium', 'Tata Power – GUGNANI TYRES', 'GLIDA DLF Bhubaneswar – Statiq', 
     'Tata Power – DN Group Corporate', 'Tata Power – MG Bhubaneswar', 'Mancheswar', 'Jaydev Vihar', 'KIIT', 
     'Tata Power – DN Wisdom Tree', 'Tata Power – GUGNANI AUTOCARS', 'Palasuni', 'Satya Nagar', 
     'TML Tirupati Enterprises'],
    # Combination 4 (Fitness 0.6479)
    ['Saheed Nagar', 'Tata Power – Regalia Mall (DN Square)', 'Sishu Bhawan', 'Tata Power – BMC Bhawani Mall', 
     'GLIDA DLF Bhubaneswar – Statiq', 'Vani Vihar', 'Nayapalli', 'HPCL – Regional Office', 
     'Tata Power – DN Group Corporate', 'Tata Power – MLCP Saheed Nagar', 'Mancheswar', 'Jagamara', 
     'Kazam – Rasulgarh', 'Tata Power – CSM Technologies', 'Tata Power – Dion Automotives', 'Pokhariput', 
     'Charger – Geetanjali', 'Tankapani Road', 'Satya Nagar', 'KIIT', 'Tata Power – GUGNANI AUTOCARS', 
     'Tata Power – Audi Bhubaneswar', 'Palasuni', 'Tata Power – GUGNANI TYRES', 'Jaydev Vihar', 
     'Tata Power – MG Bhubaneswar', 'Chandrasekharpur', 'Badagada', 'Tata Power – DN Wisdom Tree', 
     'TML Tirupati Enterprises', 'Statiq – Nexus Esplanade Mall', 'Kalinga Stadium', 
     'Statiq – Yellowings ITC Cuttack Station'],
    # Combination 5 (Fitness 0.6462)
    ['Saheed Nagar', 'Vani Vihar', 'GLIDA DLF Bhubaneswar – Statiq', 'Charger – Geetanjali', 
     'Tata Power – MG Bhubaneswar', 'Tankapani Road', 'Jaydev Vihar', 'Nayapalli', 'Kalinga Stadium', 
     'Jagamara', 'Tata Power – Dion Automotives', 'Satya Nagar', 'Tata Power – GUGNANI AUTOCARS', 
     'Tata Power – Regalia Mall (DN Square)', 'Tata Power – Audi Bhubaneswar', 'Tata Power – BMC Bhawani Mall', 
     'Tata Power – CSM Technologies', 'Palasuni', 'Badagada', 'Tata Power – MLCP Saheed Nagar', 
     'TML Tirupati Enterprises', 'Sishu Bhawan', 'Statiq – Nexus Esplanade Mall', 'Tata Power – GUGNANI TYRES', 
     'KIIT', 'Chandrasekharpur', 'Mancheswar', 'Statiq – Yellowings ITC Cuttack Station', 
     'Tata Power – DN Wisdom Tree', 'Tata Power – DN Group Corporate', 'Pokhariput', 'HPCL – Regional Office', 
     'Kazam – Rasulgarh']
]

# Coordinates for each site (latitude, longitude) - reused from original code
coordinates = {
    "Tata Power – Dion Automotives": (20.2245, 85.8330),
    "Tata Power – MG Bhubaneswar": (20.3347, 85.8038),
    "TML Tirupati Enterprises": (20.2900, 85.8200),
    "Tata Power – Regalia Mall (DN Square)": (20.2900, 85.8200),
    "Tata Power – GUGNANI TYRES": (20.2850, 85.8180),
    "Tata Power – DN Wisdom Tree": (20.2800, 85.7900),
    "Tata Power – BMC Bhawani Mall": (20.2792, 85.8412),
    "Tata Power – MLCP Saheed Nagar": (20.2792, 85.8412),
    "Tata Power – GUGNANI AUTOCARS": (20.3089, 85.8593),
    "Tata Power – CSM Technologies": (20.2910, 85.8400),
    "Tata Power – DN Group Corporate": (20.2850, 85.8180),
    "Kazam – Rasulgarh": (20.3174, 85.8463),
    "Tata Power – Audi Bhubaneswar": (20.3347, 85.8038),
    "HPCL – Regional Office": (20.2792, 85.8412),
    "Charger – Geetanjali": (20.2910, 85.8400),
    "GLIDA DLF Bhubaneswar – Statiq": (20.2700, 85.8100),
    "Statiq – Nexus Esplanade Mall": (20.3174, 85.8463),
    "Statiq – Yellowings ITC Cuttack Station": (20.3167, 85.8272),
    "Saheed Nagar": (20.2792, 85.8412),
    "Vani Vihar": (20.2910, 85.8400),
    "Jaydev Vihar": (20.2933, 85.8187),
    "Satya Nagar": (20.2811, 85.8410),
    "Tankapani Road": (20.2472, 85.8561),
    "Sishu Bhawan": (20.2598, 85.8380),
    "Nayapalli": (20.2850, 85.8180),
    "Palasuni": (20.3174, 85.8463),
    "Pokhariput": (20.2440, 85.8052),
    "Badagada": (20.2630, 85.8391),
    "Jagamara": (20.2707, 85.7917),
    "Mancheswar": (20.3089, 85.8593),
    "Kalinga Stadium": (20.2843, 85.8272),
    "KIIT": (20.3550, 85.8181),
    "Chandrasekharpur": (20.3167, 85.8272)
}

# Evaluate each combination by total pairwise distance
best_combo = None
best_dist = float('inf')

for i, combo in enumerate(top_combinations, 1):
    dist = total_distance(combo, coordinates)
    print(f"Combination {i} (Fitness {0.6598 - (i-1)*0.0033:.4f}) distance: {dist:.2f} km")
    if dist < best_dist:
        best_dist = dist
        best_combo = combo

# Final result
print("\nBest combination by total pairwise distance:")
for site in best_combo:
    print(" •", site)
print(f"Total pairwise distance: {best_dist:.2f} km")