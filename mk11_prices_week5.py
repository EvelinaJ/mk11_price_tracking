import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# reading the files with 5-week data
path = r"/Users/evelina.judeikyte/mk11_price_trackers"
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

# creating one DataFrame with all files
df = pd.concat(li, axis=0, ignore_index=True)

df = df[df["product_platform"] == "Switch"]

df.sort_values(by=["week", "retailer"])


# setting up the visual
plt.style.use("fivethirtyeight")
plt.figure(figsize=(12, 6))
plt.rcParams.update({"font.size": 12})
plt.rcParams["axes.grid"] = False

colours = ["#e74c3c", "#e74c3c", "#34495e", "#e74c3c", "#34495e", "#e74c3c"]
sns.set_palette(colours)

sns.lineplot(x="week", y="product_sale_price", hue="retailer", data=df, legend=None)

plt.xlabel("Week since launch", fontsize=11)
plt.ylabel("Price", fontsize=11)
plt.xticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5", "6"])
plt.yticks([40, 50, 60, 70, 72], ["", "49.99€", "59.99€", "69.99€", ""])

plt.text(4.65, 70.7, "Micromania", fontsize=10)
plt.text(4.65, 6, "Carrefour", fontsize=10)
plt.text(4.65, 60.7, "Auchan", fontsize=10)
plt.text(4.65, 53.7, "Amazon", fontsize=10)
plt.text(4.65, 50.7, "Galec, Fnac", fontsize=10)

plt.text(
    0.525, 74, "MK11 Switch Price at Retail: Actual vs. Recommended Price", fontsize=24
)

# saving the visual
plt.savefig("MK11 Switch Prices_weeks 1-5.png")
