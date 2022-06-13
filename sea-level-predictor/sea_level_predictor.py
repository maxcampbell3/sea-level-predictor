import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(1, figsize=(16, 9))
    plt.scatter(df['Year'], df["CSIRO Adjusted Sea Level"])
    
    
    # Create first line of best fit
    firstBestFit = linregress(x = df['Year'], y= df["CSIRO Adjusted Sea Level"])
    
    lastyear= df["Year"].max()
    df = df.append([{"Year": y}for y in range(lastyear+1,2051)])
  
    plt.plot(
      df["Year"],
      firstBestFit.intercept + firstBestFit.slope * df["Year"],
      label ='fit all',
      c = 'b',
    )
    
  
    # Create second line of best fit
  
    df_rec= df.loc[(df["Year"]>=2000) & (df["Year"]<=lastyear)]
    secbestfit = linregress(df_rec['Year'],df_rec["CSIRO Adjusted Sea Level"])
    df_rec = df_rec.append([{"Year": y}for y in range(lastyear+1,2051)])

    plt.plot(
      df_rec["Year"],
      secbestfit.intercept + secbestfit.slope * df_rec["Year"],
      label ='fit recent',
    )
    
  # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()