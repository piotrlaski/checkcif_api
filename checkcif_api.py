import requests
import re
import os

def check_http_response(response) -> None:
    if response.status_code != 200:
        return False
    else:
        return True

def get_pdf(in_cif_file:os.PathLike, out_pdf_file:os.PathLike) -> None:
    # Define the endpoint URL
    endpoint_url = r'https://checkcif.iucr.org/cgi-bin/checkcif_hkl.pl'

    # Define additional form data based on your requirements
    form_data = {
        "runtype": "symmonly",
        "referer": "checkcif_server",
        "outputtype": "PDF",  # Change as needed (HTML, PDF, etc.)
        "validtype": "checkcif_with_hkl",  # Adjust as needed
        "valout": "vrfa"}  # Adjust based on desired alert level

    # Open the file and send the POST request
    with open(in_cif_file, 'rb') as file:
        files = {"filecif": file}  # Key "filecif" based on the form's name attribute
        iucr_response = requests.post(endpoint_url, files=files, data=form_data, verify=False)

    # Check the response and scarp the pdf_url
    if check_http_response(iucr_response) is False:
        print('IUCr server not responding')
        return 0
    pdf_url = re.findall(r'//checkcif\.iucr\.org/[\w/]+/checkcif\.pdf', iucr_response.text)[0]

    #Send the GET request
    pdf_file_response = requests.get('https:' + pdf_url, verify=False)

    # Check the response and write the output file
    if check_http_response(pdf_file_response) is False:
        print('IUCr server not responding')
        return 0
    with open(out_pdf_file, 'wb') as f:
        f.write(pdf_file_response.content)

if __name__ == '__main__':
    file_path = r'C:\Users\piotr\Documents\working_dirs_lapek\checkcif_api\Rh(4-Br-SA)(CO)2__Q1_21Dlk1__CCDC.cif'
    out_path = r'test.pdf'
    get_pdf(file_path, out_path)