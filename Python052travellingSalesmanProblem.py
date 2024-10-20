def main():
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    current_path, current_distance, local_maxima, plateau, ridge = travellingSalesman(distance_matrix)
    print(current_path)
    print(current_distance)
    print(local_maxima)
    print(plateau)
    print(ridge)



def calculate_distance(path, distance_matrix):
    total = 0
    for i in range(len(path) - 1):
        total += distance_matrix[path[i]][path[i+1]]
    total += distance_matrix[path[-1]][path[0]]
    return total
    
def travellingSalesman(distance_matrix):
    current_path = [i for i in range(len(distance_matrix[0]))]
    current_distance = calculate_distance(current_path, distance_matrix)
    
    improved = True
    local_maxima = []
    plateau = []
    ridge = []
    
    while improved:
        improved = False
        best_distance = current_distance
        best_path = current_path.copy()
        
        for i in range(len(best_path)):
            for j in range(i+1 , len(best_path)):
                new_path = current_path.copy()
                new_path[i], new_path[j] = new_path[j], new_path[i]
                new_distance = calculate_distance(new_path, distance_matrix)
                
                if new_distance < best_distance:
                    best_distance = new_distance    
                    best_path = new_path
                    improved = True
        
        if not improved:
            if best_distance == current_distance:
                plateau.append((current_path, current_distance))
            else:
                local_maxima.append((current_path, current_distance))
        
        
        current_path = best_path
        current_distance = best_distance
        
    return current_path, current_distance, local_maxima, plateau, ridge


                
if __name__ == "__main__":
    main()