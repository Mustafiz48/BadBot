import os
from dotenv import load_dotenv
import google.generativeai as genai
import PIL.Image

load_dotenv()

api_key = os.getenv("google_api_key")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro-vision')


img = PIL.Image.open('images//merged.jpg')

json_format = '''{
  "seller_name":,
  "seller_address": {
    "street_address":,
    "city":,
    "postal_code":,
    "country":,
    "phone":,
    "email":,
    "fax":
  },
  "buyer_name":,
  "buyer_address":{
    "street_address":,
    "city":,
    "phone":,
    "postal_code":,
    "country":
    },
  "invoice no": ,
  "invoice_date": ,
  "po_number": ,
  "bill_to": ,
  "ship_to": ,
  "items": [
    {
      "item_description": ,
      "quantity": ,
      "unit": ,
      "unit_price":,
      "amount": 
    },
    {
      "item_description": ",
      "quantity": ,
      "unit": ,
      "unit_price": ,
      "amount": 
    },
  ],
  "subtotal": ,
  "vat": ,
  "ait": ,
  "grand_total":,
  }'''

for i in range(2):
    response = model.generate_content([f"Generate required information from the invoice in {json_format} format.", img], stream=True)
    response.resolve()
    with open("response_test.txt", 'a') as f:
        f.write(f"Response: {i}\n")
        f.write(response.text)
        f.write("\n\n")
    print(response.text)
    print("\n\n")