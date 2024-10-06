import random

# Define the possible colors and shapes
colors = ['Red', 'Blue', 'Green', 'Yellow', 'White', 'Black']
shapes = ['Tree', 'Car', 'Duck', 'Gingerbread Man', 'Rabbit', 'Pig']

# List comprehension to generate all possible items
items = [(color, shape) for color in colors for shape in shapes]  

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

# Lambda handler function
def lambda_handler(event, context):
    chosen_item = pick_item(items)
    return {
        'statusCode': 200,
        'body': chosen_item
    }