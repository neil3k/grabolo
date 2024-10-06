import random

# Define the possible colors and shapes
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange']
shapes = ['Circle', 'Square', 'Triangle', 'Star', 'Heart', 'Hexagon']

items = [(color, shape) for color in colors for shape in shapes]    # List comprehension to generate all possible items

# Function to pick an item
def pick_item(items):
    if not items:
        print("All items have been picked!")
        return None
    
    # Randomly choose an item from the available items
    chosen_item = random.choice(items)
    
    # Remove the chosen item from the list to avoid picking it again
    items.remove(chosen_item)
    
    return chosen_item

# Main game loop
def play_game():
    print("Starting Grabolo!")
    
    # Run the game until all items are picked
    while items:
        input("Press Enter to pick an item...")
        item = pick_item(items)
        if item:
            print(f"Picked item: {item}")
    
    print("Game over! All items have been picked.")

# Start the game
if __name__ == "__main__":
    play_game()