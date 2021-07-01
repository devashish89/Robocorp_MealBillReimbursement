#!/usr/bin/env python
# coding: utf-8
# %%
from veryfi import Client
from read_env_file import  get_secret_value


def get_invoice_details(file_path):
    
    # get your keys here: https://hub.veryfi.com/api/
    client_id = get_secret_value('client_id')
    client_secret = get_secret_value('client_secret')
    username = get_secret_value('veryfi_username')
    api_key = get_secret_value('api_key')
    


    veryfi_client = Client(client_id, client_secret, username, api_key)
    categories = ['Grocery', 'Utilities', 'Travel', 'Meals']
    # file_path = r"C:\Users\91836\Downloads\Food Bill\bill-converted.pdf"
    # invoicefile = r"C:\Users\91836\Downloads\Food Bill\Saturday lunch-2.pdf"
    # This submits document for processing (takes 3-5 seconds to get response)

    response = veryfi_client.process_document('bill-converted.pdf', categories=categories)
#     print(response)
    return [response['total'], response['vendor']['name'], response['vendor']['category'], response['vat_number'], response['vendor']['address']]

get_invoice_details('bill-converted.pdf')
