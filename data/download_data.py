#!/usr/bin/env python3

import yaml
import requests
import os

def main():
    # Load the config file
    with open('../src/config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    pdf_url = config['pdf_url']

    # Use requests to download the PDF
    response = requests.get(pdf_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the PDF to a file
        path = os.path.join(config['project']['root_dir'], config['data']['inbound_path'])
        with open(os.path.join(path, 'gael.pdf'), 'wb') as pdf_file:
            pdf_file.write(response.content)
        print("PDF downloaded successfully.")
    else:
        print("Failed to download PDF. Status code:", response.status_code)

if __name__ == "__main__":
    main()
