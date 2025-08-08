import pandas as pd
# Step 1: Load the data
df = pd.read_csv("netflix_titles.csv")

# Step 2: Basic Overview
print("Initial Shape:", df.shape)
print(df.info())
print(df.isnull().sum())

# Step 3: Drop duplicates
df = df.drop_duplicates()

# Step 4: Clean 'date_added' column
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df = df.dropna(subset=['date_added'])  # Remove rows with invalid dates

# Step 5: Fill missing values in 'rating' and 'country'
df['rating'] = df['rating'].fillna("Not Rated")
df['country'] = df['country'].fillna("Unknown")

# Step 6: Create new columns (Year Added, Month Added)
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month_name()

# Step 7: Split 'cast' and 'director' if needed (optional)
# e.g., Count number of cast members
df['cast_count'] = df['cast'].apply(lambda x: len(str(x).split(',')) if pd.notnull(x) else 0)

# Step 8: Save cleaned file for Power BI
df.to_csv("netflix_cleaned.csv", index=False)
print("✅ Cleaned data saved to 'netflix_cleaned.csv'")
