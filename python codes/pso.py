import math
import random

# Set random seed for different results
random.seed(123)  # Changed from default to ensure different permutations

# Stations data (33 stations/zones)
stations = [
    {"name": "Tata Power – Dion Automotives", "coords": (20.2245, 85.8330), "ev_count": 60, "grid_dist": 2.5, "cluster": 0},
    {"name": "Tata Power – MG Bhubaneswar", "coords": (20.3347, 85.8038), "ev_count": 55, "grid_dist": 3.5, "cluster": 1},
    {"name": "TML Tirupati Enterprises", "coords": (20.2900, 85.8200), "ev_count": 45, "grid_dist": 4.0, "cluster": 1},
    {"name": "Tata Power – Regalia Mall (DN Square)", "coords": (20.2900, 85.8200), "ev_count": 70, "grid_dist": 3.8, "cluster": 1},
    {"name": "Tata Power – GUGNANI TYRES", "coords": (20.2850, 85.8180), "ev_count": 65, "grid_dist": 3.2, "cluster": 1},
    {"name": "Tata Power – DN Wisdom Tree", "coords": (20.2800, 85.7900), "ev_count": 50, "grid_dist": 4.5, "cluster": 2},
    {"name": "Tata Power – BMC Bhawani Mall", "coords": (20.2792, 85.8412), "ev_count": 90, "grid_dist": 1.3, "cluster": 0},
    {"name": "Tata Power – MLCP Saheed Nagar", "coords": (20.2792, 85.8412), "ev_count": 85, "grid_dist": 1.4, "cluster": 0},
    {"name": "Tata Power – GUGNANI AUTOCARS", "coords": (20.3089, 85.8593), "ev_count": 48, "grid_dist": 5.0, "cluster": 2},
    {"name": "Tata Power – CSM Technologies", "coords": (20.2910, 85.8400), "ev_count": 75, "grid_dist": 1.6, "cluster": 0},
    {"name": "Tata Power – DN Group Corporate", "coords": (20.2850, 85.8180), "ev_count": 62, "grid_dist": 3.3, "cluster": 1},
    {"name": "Kazam – Rasulgarh", "coords": (20.3174, 85.8463), "ev_count": 50, "grid_dist": 3.7, "cluster": 1},
    {"name": "Tata Power – Audi Bhubaneswar", "coords": (20.3347, 85.8038), "ev_count": 55, "grid_dist": 3.6, "cluster": 1},
    {"name": "HPCL – Regional Office", "coords": (20.2792, 85.8412), "ev_count": 80, "grid_dist": 1.5, "cluster": 0},
    {"name": "Charger – Geetanjali", "coords": (20.2910, 85.8400), "ev_count": 70, "grid_dist": 1.7, "cluster": 0},
    {"name": "GLIDA DLF Bhubaneswar – Statiq", "coords": (20.2700, 85.8100), "ev_count": 52, "grid_dist": 4.2, "cluster": 1},
    {"name": "Statiq – Nexus Esplanade Mall", "coords": (20.3174, 85.8463), "ev_count": 68, "grid_dist": 3.8, "cluster": 1},
    {"name": "Statiq – Yellowings ITC Cuttack Station", "coords": (20.3167, 85.8272), "ev_count": 45, "grid_dist": 4.0, "cluster": 1},
    {"name": "Saheed Nagar", "coords": (20.2792, 85.8412), "ev_count": 105, "grid_dist": 1.2, "cluster": 0},
    {"name": "Vani Vihar", "coords": (20.2910, 85.8400), "ev_count": 85, "grid_dist": 1.5, "cluster": 0},
    {"name": "Jaydev Vihar", "coords": (20.2933, 85.8187), "ev_count": 72, "grid_dist": 2.0, "cluster": 0},
    {"name": "Satya Nagar", "coords": (20.2811, 85.8410), "ev_count": 57, "grid_dist": 1.8, "cluster": 0},
    {"name": "Tankapani Road", "coords": (20.2472, 85.8561), "ev_count": 51, "grid_dist": 2.7, "cluster": 0},
    {"name": "Sishu Bhawan", "coords": (20.2598, 85.8380), "ev_count": 47, "grid_dist": 2.1, "cluster": 0},
    {"name": "Nayapalli", "coords": (20.2850, 85.8180), "ev_count": 78, "grid_dist": 3.4, "cluster": 1},
    {"name": "Palasuni", "coords": (20.3174, 85.8463), "ev_count": 54, "grid_dist": 3.9, "cluster": 1},
    {"name": "Pokhariput", "coords": (20.2440, 85.8052), "ev_count": 50, "grid_dist": 4.3, "cluster": 1},
    {"name": "Badagada", "coords": (20.2630, 85.8391), "ev_count": 44, "grid_dist": 3.0, "cluster": 1},
    {"name": "Jagamara", "coords": (20.2707, 85.7917), "ev_count": 56, "grid_dist": 5.7, "cluster": 2},
    {"name": "Mancheswar", "coords": (20.3089, 85.8593), "ev_count": 46, "grid_dist": 4.9, "cluster": 2},
    {"name": "Kalinga Stadium", "coords": (20.2843, 85.8272), "ev_count": 45, "grid_dist": 5.2, "cluster": 2},
    {"name": "KIIT", "coords": (20.3550, 85.8181), "ev_count": 60, "grid_dist": 6.8, "cluster": 3},
    {"name": "Chandrasekharpur", "coords": (20.3167, 85.8272), "ev_count": 58, "grid_dist": 6.4, "cluster": 3}
]

# Haversine formula
def haversine(coord1, coord2):
    R = 6371.0  # Earth's radius
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

# Fitness function
def fitness(pos, stations):
    # Weighted EV Count (higher early)
    max_demand = 105 * sum(1 / (i + 1) for i in range(len(stations)))
    demand = sum(stations[i]["ev_count"] * (1 / (idx + 1)) for idx, i in enumerate(pos))
    demand_norm = demand / max_demand if max_demand > 0 else 0

    # Weighted Grid Distance (lower early)
    max_grid = 6.8 * sum(1 / (i + 1) for i in range(len(stations)))
    grid_dist = sum(stations[i]["grid_dist"] * (1 / (idx + 1)) for idx, i in enumerate(pos))
    grid_dist_norm = 1 - (grid_dist / max_grid) if max_grid > 0 else 0

    # Inter-site distance penalty (<0.5 km)
    penalty = 0
    for i in range(len(pos) - 1):
        dist = haversine(stations[pos[i]]["coords"], stations[pos[i+1]]["coords"])
        if dist < 0.5:
            penalty += 10

    # Cluster balance
    cluster_counts = [0] * 4  # Clusters 0, 1, 2, 3
    for i in pos:
        cluster_counts[stations[i]["cluster"]] += 1
    cluster_probs = [c / len(pos) for c in cluster_counts if c > 0]
    entropy = -sum(p * math.log2(p) for p in cluster_probs) if cluster_probs else 0
    balance_norm = entropy / math.log2(4) if entropy > 0 else 0

    # Fitness (adjusted weights for diversity)
    return 0.5 * demand_norm + 0.2 * grid_dist_norm - 0.1 * penalty + 0.2 * balance_norm

# PSO implementation
def pso(stations, swarm_size=60, iter=80, w=0.7, c1=1.5, c2=1.5, top_k=5):
    n = len(stations)
    swarm = []
    history = []

    # Initialize swarm
    for _ in range(swarm_size):
        pos = list(range(n))
        random.shuffle(pos)
        vel = [0] * n  # Initial velocity
        personal_best = pos[:]
        personal_score = fitness(pos, stations)
        swarm.append({"pos": pos, "vel": vel, "personal_best": personal_best, "personal_score": personal_score})
        history.append((personal_score, pos[:]))

    # PSO loop
    for _ in range(iter):
        # Find global best
        global_best = max(history, key=lambda x: x[0])[1]

        for particle in swarm:
            pos = particle["pos"]
            vel = particle["vel"]
            personal_best = particle["personal_best"]

            # Update velocity
            new_vel = vel[:]
            for i in range(n):
                r1, r2 = random.random(), random.random()
                new_vel[i] = (w * vel[i] +
                              c1 * r1 * (personal_best[i] - pos[i]) +
                              c2 * r2 * (global_best[i] - pos[i]))

            # Update position (more swaps for diversity)
            new_pos = pos[:]
            for _ in range(n):  # Increased swaps from n//2 to n
                i = random.randint(0, n-1)
                j = random.randint(0, n-1)
                if abs(new_vel[i]) > random.random():  # Swap if velocity is high
                    new_pos[i], new_pos[j] = new_pos[j], new_pos[i]

            # Evaluate new position
            score = fitness(new_pos, stations)
            if score > particle["personal_score"]:
                particle["personal_best"] = new_pos[:]
                particle["personal_score"] = score
            particle["pos"] = new_pos
            particle["vel"] = new_vel
            history.append((score, new_pos[:]))

    # Extract top-K unique permutations
    unique_history = []
    seen = set()
    for score, pos in sorted(history, key=lambda x: x[0], reverse=True):
        pos_tuple = tuple(pos)
        if pos_tuple not in seen:
            seen.add(pos_tuple)
            unique_history.append((score, pos))
        if len(unique_history) >= top_k:
            break

    return [(score, [stations[i]["name"] for i in pos]) for score, pos in unique_history]

# Run PSO and print results
if __name__ == "__main__":
    results = pso(stations)
    for rank, (score, permutation) in enumerate(results, 1):
        print(f"\nCombination {rank} (Fitness {score:.4f})")
        print(permutation)
        