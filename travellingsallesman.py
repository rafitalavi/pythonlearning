import itertools

def calculate_distance(points, order):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += points[order[i]][order[i + 1]]
    total_distance += points[order[-1]][order[0]]  # Return to the starting city
    return total_distance

def traveling_salesman(points):
    cities = list(range(len(points)))
    shortest_distance = float('inf')
    shortest_path = None

    for perm in itertools.permutations(cities):
        distance = calculate_distance(points, perm)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = perm

    return shortest_distance, shortest_path

if __name__ == "__main__":
    num_cities = int(input("Enter the number of cities: "))

    points = []
    for i in range(num_cities):
        x, y = map(int, input(f"Enter coordinates (x y) for city {i+1}: ").split())
        points.append((x, y))

    distances = [[0 for _ in range(num_cities)] for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2) ** 0.5

    shortest_distance, shortest_path = traveling_salesman(distances)

    print(f"\nShortest distance: {shortest_distance}")
    print("Shortest path:", "->".join([str(city + 1) for city in shortest_path]))
