import requests
import re

# Define the endpoint URL
endpoint_url = r'https://checkcif.iucr.org/cgi-bin/checkcif_hkl.pl'

# Define the file to upload
file_path = r'C:\Users\piotr\Documents\working_dirs_lapek\checkcif_api\Rh(4-Br-SA)(CO)2__Q1_21Dlk1__CCDC.cif'

# Define additional form data based on your requirements
form_data = {
    "runtype": "symmonly",
    "referer": "checkcif_server",
    "outputtype": "PDF",  # Change as needed (HTML, PDF, etc.)
    "validtype": "checkcif_with_hkl",  # Adjust as needed
    "valout": "vrfa",  # Adjust based on desired alert level
}

# Open the file and send the POST request
with open(file_path, 'rb') as file:
    files = {"filecif": file}  # Key "filecif" based on the form's name attribute
    response = requests.post(endpoint_url, files=files, data=form_data, verify=False)

# Check the response
if response.status_code == 200:
    print("File uploaded and processed successfully.")
    # If the response contains the result, you can save or process it here
else:
    print("Error uploading or processing the file:", response.status_code)
    print("Response content:", response.text)

pdf_url = re.findall(r'//checkcif\.iucr\.org/[\w/]+/checkcif\.pdf', response.text)[0]

pdf_file = requests.get('https:' + pdf_url, verify=False)

with open('output.pdf', 'wb') as f:
    f.write(pdf_file.content)  # Write the content to the file

