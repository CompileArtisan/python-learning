def main():
    initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]  # 0 represents the blank space
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]    # Goal is to arrange the numbers in order
    
    current_state, moves_made, local_maxima, plateau, ridge = eightPuzzle(initial_state, goal_state)
    print("Final State:")
    for row in current_state:
        print(row)
    print("Moves made:", moves_made)
    print("Local Maxima:", local_maxima)
    print("Plateau:", plateau)
    print("Ridge:", ridge)

def apply_move(state, move):
    new_state = [row[:] for row in state]
    zero_pos = find_zero(state)
    i, j = zero_pos
    di, dj = move
    
    new_state[i][j], new_state[i + di][j + dj] = new_state[i + di][j + dj], new_state[i][j]
    return new_state

def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def is_better_state(new_state, goal_state, current_state):
    return heuristic(new_state, goal_state) < heuristic(current_state, goal_state)

def heuristic(state, goal_state):
    misplaced_tiles = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                misplaced_tiles += 1
    return misplaced_tiles

def eightPuzzle(initial_state, goal_state):
    current_state = initial_state
    moves_made = 0
    
    improved = True
    local_maxima = []
    plateau = []
    ridge = []
    

    while improved:
        improved = False
        best_state = current_state
        possible_moves = generate_possible_moves(current_state)
        
        for move in possible_moves:
            new_state = apply_move(current_state, move)
            if is_better_state(new_state, goal_state, current_state):
                best_state = new_state
                improved = True
        
        if not improved:
            if current_state == best_state:
                plateau.append((current_state, moves_made))
            else:
                local_maxima.append((current_state, moves_made))
        
        current_state = best_state
        moves_made += 1
        
    return current_state, moves_made, local_maxima, plateau, ridge

def generate_possible_moves(state):
    moves = []
    zero_pos = find_zero(state)
    i, j = zero_pos
    
    if i > 0:
        moves.append((-1, 0))  # Move blank up
    if i < 2:
        moves.append((1, 0))   # Move blank down
    if j > 0:
        moves.append((0, -1))  # Move blank left
    if j < 2:
        moves.append((0, 1))   # Move blank right
    
    return moves


if __name__ == "__main__":
    main()
