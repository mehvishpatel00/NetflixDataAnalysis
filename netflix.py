import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset
data = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\NetflixAnalysis\netflix1.csv")

print(data.head()) #informtn

# Data Information
print(data.info())
print(data.shape)

# Drop duplicates
data = data.drop_duplicates()

# Content distribution on Netflix
type_counts = data['type'].value_counts()
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
sns.countplot(data=data, x='type', ax=axes[0])
plt.pie(type_counts, labels=['Movie', 'TV Show'], autopct='%.0f%%')
plt.suptitle('Total Content on Netflix', fontsize=20)
plt.show()

# Rating frequency
data['rating'].value_counts().plot(kind='bar', figsize=(10, 6))
plt.xticks(rotation=45, ha='right')
plt.xlabel("Rating Types")
plt.ylabel("Rating Frequency")
plt.title('Rating on Netflix')
plt.show()

# Convert 'date_added' to datetime
data['date_added'] = pd.to_datetime(data['date_added'])
print(data.describe())

# Top 10 countries with most content
top_ten_countries = data['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.bar(top_ten_countries.index, top_ten_countries.values)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Country")
plt.ylabel("Frequency")
plt.title("Top 10 countries with most content on Netflix")
plt.show()

# Monthly releases
data['year'] = data['date_added'].dt.year
data['month'] = data['date_added'].dt.month
data['day'] = data['date_added'].dt.day
monthly_movie_release = data[data['type'] == 'Movie']['month'].value_counts().sort_index()
monthly_series_release = data[data['type'] == 'TV Show']['month'].value_counts().sort_index()
plt.plot(monthly_movie_release.index, monthly_movie_release.values, label='Movies')
plt.plot(monthly_series_release.index, monthly_series_release.values, label='Series')
plt.xlabel("Months")
plt.ylabel("Frequency of releases")
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)
plt.title("Monthly releases of Movies and TV shows on Netflix")
plt.show()

# Yearly releases
yearly_movie_releases = data[data['type'] == 'Movie']['year'].value_counts().sort_index()
yearly_series_releases = data[data['type'] == 'TV Show']['year'].value_counts().sort_index()
plt.plot(yearly_movie_releases.index, yearly_movie_releases.values, label='Movies')
plt.plot(yearly_series_releases.index, yearly_series_releases.values, label='TV Shows')
plt.xlabel("Years")
plt.ylabel("Frequency of releases")
plt.grid(True)
plt.title("Yearly releases of Movies and TV Shows on Netflix")
plt.legend()
plt.show()

# Top 10 popular genres for movies
popular_movie_genre = data[data['type'] == 'Movie'].groupby("listed_in").size().sort_values(ascending=False)[:10]
plt.bar(popular_movie_genre.index, popular_movie_genre.values)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Genres")
plt.ylabel("Movies Frequency")
plt.title("Top 10 popular genres for movies on Netflix")
plt.show()

# Top 10 popular genres for TV Shows
popular_series_genre = data[data['type'] == 'TV Show'].groupby("listed_in").size().sort_values(ascending=False)[:10]
plt.bar(popular_series_genre.index, popular_series_genre.values)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Genres")
plt.ylabel("TV Shows Frequency")
plt.title("Top 10 popular genres for TV Shows on Netflix")
plt.show()

# Top 15 directors with highest frequency of movies and shows
directors = data['director'].value_counts().head(15)
plt.bar(directors.index, directors.values)
plt.xticks(rotation=45, ha='right')
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.title("Top 15 Directors with the Most Titles")
plt.show()
