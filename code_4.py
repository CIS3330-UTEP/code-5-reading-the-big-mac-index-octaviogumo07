import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    # Filter the DataFrame for the specific year and country code, 'date' starts with the year, 'iso_a3' country code matches
    filtered_df = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'] == country_code.upper())] #generated with the help of AI
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None #if it is empty return none
    
    # Calculate the mean of the 'dollar_price' column
    mean_price = filtered_df['dollar_price'].mean()
    
    # Round the mean price to 2 decimal places
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    # Filter the DataFrame for the specific country code, filters all rows for the country and ignores the year
    filtered_df = df[df['iso_a3'] == country_code.upper()] #generated with the help of AI
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None #if no data exists return none
    
    # Calculate the mean of the 'dollar_price' column
    mean_price = filtered_df['dollar_price'].mean()
    
    # Round the mean price to 2 decimal places
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year): #finding the country with the cheapest price
    # Filter the DataFrame for the specific year
    filtered_df = df[df['date'].str.startswith(str(year))] #filters all rows from that year
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None
    
    # Find the row with the minimum 'dollar_price'
    cheapest = filtered_df.loc[filtered_df['dollar_price'].idxmin()]
    
    # Format the output string
    return f"{cheapest['name']}({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}" #formats the results to show country name, ISO code and price, generated with the help of AI

def get_the_most_expensive_big_mac_price_by_year(year):
    # Filter the DataFrame for the specific year
    filtered_df = df[df['date'].str.startswith(str(year))]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None #if empty return 'None'
    
    # Find the row with the maximum 'dollar_price' using .idmax()
    most_expensive = filtered_df.loc[filtered_df['dollar_price'].idxmax()] #generated with the help of AI 
    
    # Format the output string
    return f"{most_expensive['name']}({most_expensive['iso_a3']}): ${round(most_expensive['dollar_price'], 2)}" #generated with the help of AI

if __name__ == "__main__":
    year = 2020
    country_code = 'usa'

    print(f"Mean Big Mac price in {year} for {country_code}: ${get_big_mac_price_by_year(year, country_code)}")
    print(f"Mean Big Mac price for {country_code}: ${get_big_mac_price_by_country(country_code)}")
    print(f"Cheapest Big Mac in {year}: {get_the_cheapest_big_mac_price_by_year(year)}")
    print(f"Most expensive Big Mac in {year}: {get_the_most_expensive_big_mac_price_by_year(year)}")

    #OpenAI. (2025). ChatGPT (Version GPT-4). https://chat.openai.com/
    #This code was developed with assistance from ChatGPT (GPT-4), an AI language model created by OpenAI.


