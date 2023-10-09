import json
import matplotlib.pyplot as plt
import requests
with open('C:\\Users\\ANDY\\Desktop\\download\\csci-526\\11\\mazeshift-marauders-67598-default-rtdb-export.json', 'r') as file:
    data = json.load(file)


    # Parse data from JSON
    player_ids = list(data['Player'].keys())
    ages = [entry['age'] for entry in data['Player'].values()]

    # Plotting
    plt.figure(figsize=(10, 6))

    plt.bar(player_ids, ages, color=['blue', 'green'])  # Use different colors for each bar
    plt.title("Ages of Players")
    plt.xlabel("Player IDs")
    plt.ylabel("Age")
    plt.xticks(rotation=45)  # Rotate x labels for better visibility
    plt.tight_layout()
    plt.show()