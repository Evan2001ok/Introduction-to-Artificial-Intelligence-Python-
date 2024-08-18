import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

table1 = pd.read_csv("./Downloads/AAPL.csv")
table1 = table1.head(10)
base_color = sb.color_palette("colorblind")[0] 
sb.countplot(data = table1, x = "High", color = base_color);
plt.show()