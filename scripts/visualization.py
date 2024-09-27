import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# Function to plot bar charts for population data
def plot_population(data, title, color, edgecolor):
    plt.figure(figsize=(10, 6))
    plt.bar(data['Country'], data['Population'], width=0.8, color=color, edgecolor=edgecolor)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.ylabel('Total Population', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# Function to plot bar charts for population data
def plot_gender(data, title, color, edgecolor):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Population', y='Country', data=data, hue='Country', palette=color, edgecolor=edgecolor)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Total Population', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()