import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    # Filter the DataFrame for the specific year and country code
    filtered_df = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'] == country_code.upper())]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None
    
    # Calculate the mean of the 'dollar_price' column
    mean_price = filtered_df['dollar_price'].mean()
    
    # Round the mean price to 2 decimal places
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    # Filter the DataFrame for the specific country code
    filtered_df = df[df['iso_a3'] == country_code.upper()]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None
    
    # Calculate the mean of the 'dollar_price' column
    mean_price = filtered_df['dollar_price'].mean()
    
    # Round the mean price to 2 decimal places
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    # Filter the DataFrame for the specific year
    filtered_df = df[df['date'].str.startswith(str(year))]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None
    
    # Find the row with the minimum 'dollar_price'
    cheapest = filtered_df.loc[filtered_df['dollar_price'].idxmin()]
    
    # Format the output string
    return f"{cheapest['name']}({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    # Filter the DataFrame for the specific year
    filtered_df = df[df['date'].str.startswith(str(year))]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None
    
    # Find the row with the maximum 'dollar_price'
    most_expensive = filtered_df.loc[filtered_df['dollar_price'].idxmax()]
    
    # Format the output string
    return f"{most_expensive['name']}({most_expensive['iso_a3']}): ${round(most_expensive['dollar_price'], 2)}"

if __name__ == "__main__":
    year = 2020
    country_code = 'usa'

    print(f"Mean Big Mac price in {year} for {country_code}: ${get_big_mac_price_by_year(year, country_code)}")
    print(f"Mean Big Mac price for {country_code}: ${get_big_mac_price_by_country(country_code)}")
    print(f"Cheapest Big Mac in {year}: {get_the_cheapest_big_mac_price_by_year(year)}")
    print(f"Most expensive Big Mac in {year}: {get_the_most_expensive_big_mac_price_by_year(year)}")

import pandas as pd
import matplotlib.pyplot as plt

#installing Matplotlib
filename = "./big-mac-full-index.csv"
df = pd.read_csv(filename)

#filter for data in Argentina
smol_df = df.query("iso_a3 == 'ARG'")

#create the scatter plot
smol_df.plot.scatter(x="date", y="dollar_price")
plt.show()