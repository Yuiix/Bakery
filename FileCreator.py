import os
import shutil
import json


def create_files_with_sells():
    # Define the folder path
    folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Ventas')

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Clean up the contents of the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

    # Define a function to format the JSON data
    def format_data(data):
        # Extract the values from the JSON data
        value1 = data['total_sold']["total"]
        value2 = data['bread_quantities']["bread_quantity_1"]
        value3 = data['bread_quantities']["bread_quantity_2"]
        value4 = data['bread_quantities']["bread_quantity_3"]
        value5 = data['bread_quantities']["bread_quantity_4"]

        # Format the values into a string
        formatted_string = f"El dia de hoy vendiste en total: {value1} MX$\nDel pan #1 te sobró: {value2} pza" \
                           f"\nDel pan #2 te sobró: {value3} pza\nDel pan #3 te sobró: {value4} pza" \
                           f"\nDel pan #4 te sobró: {value5} pza\n"

        return formatted_string

    # Dump data from JSON files to text files
    for filename in os.listdir():
        if filename.endswith('.json'):
            if not filename.startswith('data'):
                with open(filename, 'r') as json_file:
                    data = json.load(json_file)
                txt_filename = os.path.join(folder_path, f"{filename[:-5]}.txt")
                with open(txt_filename, 'w') as txt_file:
                    formatted_data = format_data(data)
                    txt_file.write(formatted_data)
