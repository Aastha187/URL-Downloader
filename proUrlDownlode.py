import tkinter as tk

def take_input():
    url = entry.get()  # Get text from the entry box
    file_name = entry2.get()  # Get filename from the second entry box
    download_file(url, file_name)  # Call download_file with user inputs

# Create the main window
root = tk.Tk()
root.title("Simple Input and Button GUI")
root.geometry("300x250")  # Set the window size

# Create and pack label
label = tk.Label(root, text="Enter URL:")
label.pack(pady=10)

# Create and pack entry for URL
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Create and pack label for filename
label2 = tk.Label(root, text="Enter filename:")
label2.pack(pady=10)

# Create and pack entry for filename
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

# Create and pack button with command to call take_input
button = tk.Button(root, text="Submit", command=take_input)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
import requests
def download_file(url,file_name):
    response=requests.get(url)
    if response.status_code == 200:
        with open(file_name,'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. status code: {response.status_code}")
if _name=="main_":
    url="https://github.com/upessocs/B1B2/blob/main/fileOrganizerGui/Organizer.zip"
    file_name='Organizer.zip'
    download_file(url,file_name)