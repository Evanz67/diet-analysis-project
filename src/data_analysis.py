import pandas as pd
import matplotlib.pyplot as plt

# Load the csv data
df = pd.read_csv('All_Diets.csv')

# Value handling
#df.fillna(0, inplace=True) # I saw the pseudocode that we need to fill it using mean but just incase something goes wrong I am just gonna put this one here to fill it with zeroes instead
df.fillna(df.mean(numeric_only=True), inplace=True) #This line uses mean for filling the data

# The average macronutrient for each diet
print("Average nutrients by diet:")
print(df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean())

print("<--------------------------------------------------------------------------------------------------------->")

# The top protein for each diet
print("\n\nTop protein recipes by diet:")
for diet in df['Diet_type'].unique():
    top = df[df['Diet_type'] == diet].nlargest(5, 'Protein(g)')
    print(f"\n{diet}: {top['Recipe_name'].values}")

print("<--------------------------------------------------------------------------------------------------------->")

# The highest protein diet
highest = df.groupby('Diet_type')['Protein(g)'].mean().idxmax()
print(f"\nHighest protein diet: {highest}")

print("<--------------------------------------------------------------------------------------------------------->")

# Common Cuisine
print("\nMost common cuisines:")
for diet in df['Diet_type'].unique():
    common = df[df['Diet_type'] == diet]['Cuisine_type'].value_counts().index[0]
    print(f"{diet}: {common}")

# Add the new ratio to pandas
df['Protein_to_Carbs'] = df['Protein(g)'] / df['Carbs(g)']
df['Carbs_to_Fat'] = df['Carbs(g)'] / df['Fat(g)']

# Bar Chart
average = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
average.plot(kind='bar', figsize=(10, 5))
plt.title('Average Nutrients by Diet Type')
plt.ylabel('Grams (g)')
plt.tight_layout()
plt.show()

# Heatmap
plt.figure(figsize=(8, 4))
dietMeans = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
plt.imshow(dietMeans, cmap='Blues', aspect='auto')
plt.colorbar(label='Grams')
plt.xticks(range(3), ['Protein', 'Carbs', 'Fat'])
plt.yticks(range(len(dietMeans)), dietMeans.index)
plt.title('Relationship of Diet Type and Macronutrients')
plt.tight_layout()
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 5))
top5Protein = df.nlargest(5, 'Protein(g)')
plt.scatter(range(len(top5Protein)), top5Protein['Protein(g)'])
plt.xticks(range(len(top5Protein)), top5Protein['Recipe_name'], rotation=45)
plt.title('Top 5 Protein Recipes across different cuisine')
plt.ylabel('Protein (g)')
plt.tight_layout()
plt.show()

