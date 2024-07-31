import matplotlib.pyplot as plt
import json

def load_processed_data(file_path):
    """Load processed data from JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def create_bar_chart(data):
    """Create a bar chart from the provided data."""
    labels = data.keys()
    values = data.values()

    plt.bar(labels, values)
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.title('Event Counts')
    plt.show()

if __name__ == '__main__':
    data = load_processed_data('data/processed_data.json')
    create_bar_chart(data)
