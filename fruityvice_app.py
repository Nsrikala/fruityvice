import streamlit
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #just writes the data to screen

#take the Json version of responce and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output the screan as a table
streamlit.dataframe(fruitvice_normalized)

