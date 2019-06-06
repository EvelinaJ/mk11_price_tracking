import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# AMAZON
# importing amazon data
amazon_df = pd.read_csv("mk11_amazon/amazon_week5.csv")

# cleaning the data
# standardising titles
map_titles_amzn = {"Mortal Kombat 11: Standard Edition":"Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11: Premium Edition":"Mortal Kombat 11: Premium Edition",
              "Mortal Kombat 11 - Kollector's Edition": "Mortal Kombat 11: Kollector Edition",
              "Mortal Kombat 11 - Kollector Edition": "Mortal Kombat 11: Kollector Edition"}
amazon_df["product_name"] = amazon_df["product_name"].map(map_titles_amzn)

# renaming platforms and removing commas
map_platforms_amzn = {"Xbox One":"XONE", "PlayStation 4":"PS4",
                 "Nintendo Switch":"Switch", "Windows 10":"PC"}
amazon_df["product_platform"] = amazon_df["product_platform"].str.replace(",", "")
amazon_df["product_platform"] = amazon_df["product_platform"].map(map_platforms_amzn)

# removing unnecessary items in the price
amazon_df["product_sale_price"] = (amazon_df["product_sale_price"]
                                  .str.replace(",", ".")
                                  .str.replace("EUR ", "")
                                  )

# adding a retailer column that will serve in the later merge
amazon_df["retailer"] = "amazon"


# AUCHAN
# importing auchan data
auchan_df = pd.read_csv("mk11_auchan/auchan_week5.csv")

# cleaning the data
# standardising titles
map_titles_auch = {"Mortal Kombat 11 PS4":"Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Xbox One":"Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Nintendo Switch":"Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Edition Premium PS4":"Mortal Kombat 11: Premium Edition",
              "Mortal Kombat 11 Edition Premium Xbox One":"Mortal Kombat 11: Premium Edition",
              "Mortal Kombat 11 Edition Kollector PS4": "Mortal Kombat 11: Kollector Edition",
              "Mortal Kombat 11 Edition Kollector Xbox One": "Mortal Kombat 11: Kollector Edition"}
auchan_df["product_name"] = auchan_df["product_name"].map(map_titles_auch)

# renaming platforms
map_platforms_auch = {"Xbox One":"XONE", "PS4":"PS4",
                 "Switch":"Switch"}
auchan_df["product_platform"] = auchan_df["product_platform"].map(map_platforms_auch)

# removing unnecessary items in the price
auchan_df["product_sale_price"] = (auchan_df["product_sale_price"]
                                  .str.replace(",", ".")
                                  .str.replace(" €", "")
                                  )

auchan_df["retailer"] = "auchan"


# CARREFOUR
# importing carrefour data
carrefour_df = pd.read_csv("mk11_carrefour/carrefour_week5.csv")

# cleaning the data
# standardising titles
map_titles_crf = {"Mortal Kombat 11 PS4 WARNER BROS. INTERACTIVE ENTERTAINMENT":"Mortal Kombat 11: Standard Edition",
              "MORTAL KOMBAT 11 Xbox One WARNER BROS. INTERACTIVE ENTERTAINMENT":"Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Switch WARNER BROS. INTERACTIVE ENTERTAINMENT": "Mortal Kombat 11: Standard Edition"
              }
carrefour_df["product_name"] = carrefour_df["product_name"].map(map_titles_crf)

# adding platforms as they were unavailable on the website
carrefour_df["product_platform"] = ["PS4", "XONE", "Switch"]

# removing unnecessary items in the price
carrefour_df["product_sale_price"] = (carrefour_df["product_sale_price"]
                                  .str.replace(",", ".")
                                  .str.replace("€", "")
                                  )
carrefour_df["retailer"] = "carrefour"


# GALEC
# importing galec data
galec_df = pd.read_csv("mk11_galec/galec_week5.csv")

# cleaning the data
# standardising titles
map_titles_gal = {"Mortal kombat 11 - édition standard (PS4)": "Mortal Kombat 11: Standard Edition",
              "Mortal kombat 11 - édition standard (XBOXONE)": "Mortal Kombat 11: Standard Edition",
              "Mortal kombat 11 - édition standard (SWITCH)": "Mortal Kombat 11: Standard Edition",
              "Mortal kombat 11 - édition premium (PS4)": "Mortal Kombat 11: Premium Edition",
              "Mortal kombat 11 - édition premium (XBOXONE)": "Mortal Kombat 11: Premium Edition",
              "Mortal kombat 11 - édition collector (PS4)": "Mortal Kombat 11: Kollector Edition",
              "Mortal kombat 11 - édition collector (XBOXONE)": "Mortal Kombat 11: Kollector Edition",
              "Mortal kombat 11 - édition collector (PC)": "Mortal Kombat 11: Kollector Edition"}
galec_df["product_name"] = galec_df["product_name"].map(map_titles_gal)

# renaming platforms
map_platforms_gal = {"Microsoft XBox One":"XONE", "Sony PlayStation 4":"PS4",
                 "Nintendo Switch":"Switch", "PC (Windows)": "PC"}
galec_df["product_platform"] = galec_df["product_platform"].map(map_platforms_gal)

# removing unnecessary items in the price
galec_df["product_sale_price"] = (galec_df["product_sale_price"].str.replace(",", "."))

galec_df["retailer"] = "galec"


# MICROMANIA
# importing micromania data
micro_df = pd.read_csv("mk11_micro/micro_week5.csv")

# cleaning the data
# standardising titles
map_titles_mic = {"Mortal Kombat 11 Edition Steelbook (Exclusivité MICROMANIA) PS4": "Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Edition Steelbook (Exclusivité MICROMANIA) XBOX ONE": "Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 SWITCH": "Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Premium Edition PS4": "Mortal Kombat 11: Premium Edition",
              "Mortal Kombat 11 Premium Edition XBOX ONE": "Mortal Kombat 11: Premium Edition",
              "Mortal Kombat 11 Edition Kollector PS4": "Mortal Kombat 11: Kollector Edition",
              "Mortal Kombat 11 Edition Kollector XBOX ONE": "Mortal Kombat 11: Kollector Edition",
              }
micro_df["product_name"] = micro_df["product_name"].map(map_titles_mic)

# renaming platforms 
map_platforms_mic = {"XBOX ONE":"XONE", "PS4":"PS4",
                 "SWITCH":"Switch"}
micro_df["product_platform"] = micro_df["product_platform"].map(map_platforms_mic)

# removing unnecessary items in the price
micro_df["product_sale_price"] = (micro_df["product_sale_price"]
                                 .str.replace(",", ".")
                                 .str.replace(" ", "")
                                 .str.replace("\xa0€", "")
                                 .str.replace("€", "")
                                 )

micro_df["retailer"] = "micromania"


# FNAC
# importing fnac data
fnac_df = pd.read_csv("mk11_fnac/fnac_week5.csv")

# cleaning the data
# standardising titles
map_titles_fnac = {"Mortal Kombat 11 PS4": "Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Xbox One": "Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Nintendo Switch": "Mortal Kombat 11: Standard Edition",
              "Mortal Kombat 11 Edition Premium PS4": "Mortal Kombat 11: Premium Edition",
              "Mortal Kombat 11 Edition Premium Xbox One": "Mortal Kombat 11: Premium Edition",
              "Mortal Kombat 11 Kollector's Edition PS4": "Mortal Kombat 11: Kollector Edition",
              "Mortal Kombat 11 Kollector's Edition Xbox One": "Mortal Kombat 11: Kollector Edition",
              "Mortal Kombat 11 Kollector's Edition PC": "Mortal Kombat 11: Kollector Edition"}
fnac_df["product_name"] = fnac_df["product_name"].map(map_titles_fnac)

# renaming platforms 
map_platforms_fnac = {"Xbox One":"XONE", "PlayStation 4":"PS4",
                 "Nintendo Switch":"Switch", "PC": "PC"}
fnac_df["product_platform"] = fnac_df["product_platform"].map(map_platforms_fnac)

# removing unnecessary items in the price
# adding .99€ that were too complicated to extract from the website directly
# fnac_df["product_sale_price"] = (fnac_df["product_sale_price"].str.replace("€", ""))
fnac_df["product_sale_price"] = fnac_df["product_sale_price"] + 0.99

fnac_df["retailer"] = "fnac"


# concatenate all DataFrames
list_of_df = [amazon_df, auchan_df, carrefour_df, galec_df, micro_df, fnac_df]
mk11_prices_all = pd.concat(list_of_df)

# adding recommended retail price column
mk11_prices_all["rrp"] = 0
mk11_prices_all.loc[mk11_prices_all["product_name"]=="Mortal Kombat 11: Standard Edition", 
                    "rrp"] = 69.99
mk11_prices_all.loc[mk11_prices_all["product_name"]=="Mortal Kombat 11: Premium Edition", 
                    "rrp"] = 99.99
mk11_prices_all.loc[mk11_prices_all["product_name"]=="Mortal Kombat 11: Kollector Edition", 
                    "rrp"] = 299.99

# setting prices as float
mk11_prices_all["product_sale_price"] = mk11_prices_all["product_sale_price"].astype(float)
mk11_prices_all["rrp"] = mk11_prices_all["rrp"].astype(float)

# adding a column with week number
mk11_prices_all["week"] = 5

# exporting files
mk11_prices_all.to_csv("mk11_prices_week5.csv", index=False)

# plotting the standard edition prices for Switch
# creating a DataFrame for Switch edition
mk11_switch = mk11_prices_all[mk11_prices_all["product_platform"]=="Switch"]
mk11_switch = mk11_switch.sort_values(by="product_sale_price", ascending=False)
# adding a day column to track price changes over time

# setting up a barplot
plt.style.use("fivethirtyeight")
plt.figure(figsize=(12,6))
plt.rcParams.update({'font.size': 12})
plt.rcParams['axes.grid'] = False

colours = ["#34495e", "#34495e", "#e74c3c", "#e74c3c", "#e74c3c", "#e74c3c"]
sns.set_palette(colours)

sns.barplot(x="retailer", y="product_sale_price", data=mk11_switch)
sns.lineplot(x="retailer", y="rrp", data=mk11_switch) 

plt.xlabel("")
plt.ylabel("Current Sale Price", fontsize=10)
plt.xticks([0, 1, 2, 3, 4, 5], ["Micromania", "Carrefour", "Auchan", "Amazon", "E.Leclerc", "Fnac"])
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80],["", "9.99€", "19.99€", "29.99€", "39.99€", "49.99€", "59.99€", "69.99€", ""])
plt.annotate("Recommended Price", xy=(3.1,65), xytext=(4.1,72), fontsize=10) 
plt.annotate("Mortal Kombat 11 Switch: Actual vs. Recommended Price, Week 5", 
             xy=(-0,0), xytext=(-0.96,80), fontsize=20) 

plt.savefig("MK11 Switch Prices_week5.png")

