import random

def expected_raids_combined(probability):
    return 1 / probability

def calculate_combined_probability(items, item_data):
    combined_probability = 0
    for item in items:
        combined_probability += item_data[item]['drop_rate']
    return combined_probability

def select_item_based_on_probability(items, item_data):
    total_probability = sum(item_data[item]['drop_rate'] for item in items)
    selection_point = random.uniform(0, total_probability)
    current_sum = 0
    for item in items:
        current_sum += item_data[item]['drop_rate']
        if current_sum >= selection_point:
            return item

def calculate_average_raids_to_get_items(items, item_data):
    raid_success_chance = 0.65
    total_expected_raids = 0
    remaining_items = items.copy()
    
    while remaining_items:
        combined_probability = calculate_combined_probability(remaining_items, item_data) * raid_success_chance
        expected_raids_for_combined = expected_raids_combined(combined_probability)
        total_expected_raids += expected_raids_for_combined
        
        # Select and remove an item based on the drop rates
        obtained_item = select_item_based_on_probability(remaining_items, item_data)
        remaining_items.remove(obtained_item)
        
    return total_expected_raids

# Provided data
item_data = {
    "Dexterous prayer scroll": {"drop_rate": 20/69, "value": 16256648},
    "Arcane prayer scroll": {"drop_rate": 20/69, "value": 2758859},
    "Twisted buckler": {"drop_rate": 4/69, "value": 20541591},
    "Dragon hunter crossbow": {"drop_rate": 4/69, "value": 63339808},
    "Dinh's bulwark": {"drop_rate": 3/69, "value": 22204372},
    "Ancestral hat": {"drop_rate": 3/69, "value": 59006065},
    "Ancestral robe top": {"drop_rate": 3/69, "value": 178768971},
    "Ancestral robe bottom": {"drop_rate": 3/69, "value": 136303622},
    "Dragon claws": {"drop_rate": 3/69, "value": 96023576},
    "Elder maul": {"drop_rate": 2/69, "value": 140324174},
    "Kodai insignia": {"drop_rate": 2/69, "value": 117478791},
    "Twisted bow": {"drop_rate": 2/69, "value": 1670378600}
}

# Example usage
items_to_obtain = ["Twisted bow", "Kodai insignia", "Ancestral robe top"]
average_raids = calculate_average_raids_to_get_items(items_to_obtain, item_data)
print(f"Average number of raids to get {items_to_obtain}: {average_raids:.2f}")

# You can change the items_to_obtain list to calculate for different sets of items
