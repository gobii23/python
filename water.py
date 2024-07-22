class State:
    def _init_(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def _eq_(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def _hash_(self):
        return hash((self.jug1, self.jug2))

    def _repr_(self):
        return f"({self.jug1}, {self.jug2})"


def is_goal(state, goal):
    return state.jug1 == goal or state.jug2 == goal


def pour(state, max_jug1, max_jug2, visited, goal):
    visited.add(state)
    if is_goal(state, goal):
        return True

    actions = [
        (max_jug1, state.jug2), 
        (state.jug1, max_jug2),  
        (0, state.jug2),        
        (state.jug1, 0),    
        (min(state.jug1 + state.jug2, max_jug1), state.jug2 - (min(state.jug1 + state.jug2, max_jug1) - state.jug1)),  # Pour jug2 into jug1
        (state.jug1 - (min(state.jug1 + state.jug2, max_jug2) - state.jug2), min(state.jug1 + state.jug2, max_jug2))   # Pour jug1 into jug2
    ]

    for action in actions:
        next_state = State(*action)
        if next_state not in visited:
            if pour(next_state, max_jug1, max_jug2, visited, goal):
                print(next_state)
                return True
    return False


def water_jug_problem(jug1, jug2, goal):
    initial_state = State(0, 0)
    max_jug1 = jug1
    max_jug2 = jug2
    visited = set()

    if pour(initial_state, max_jug1, max_jug2, visited, goal):
        print(f"\nGoal of {goal} liters reached!")
    else:
        print("\nGoal not possible with given jugs and goal.")

water_jug_problem(4, 3, 2)

