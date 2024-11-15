import pandas as pd
import re


# Function to load and explore the dataset
def loadnexplore_data(file_path):
    df = pd.read_csv(file_path)
    print("Initial Data Exploration:")
    print(df.info())
    print(df.head())
    return df

# Function to handle missing values
def handle_missing_values(df):
    print("\nMissing Values Before Handling:")
    print(df.isnull().sum())
    df.fillna({'likes': 0, 'retweets': 0, 'hashtags': '', 'message': ''}, inplace=True)
    print("\nMissing Values After Handling:")
    print(df.isnull().sum())
    return df

# Function to correct data types
def correct_dt(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['likes'] = df['likes'].astype(int)
    df['retweets'] = df['retweets'].astype(int)
    return df

# Function to remove duplicates
def remove_duplicates(df):
    print("\nNumber of Duplicates Before Removal:", df.duplicated().sum())
    df.drop_duplicates(inplace=True)
    print("Number of Duplicates After Removal:", df.duplicated().sum())
    return df

# Function to clean text fields
def clean_fields(df):
    df['message'] = df['message'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())
    return df

# Function to save the cleaned dataset
def save_cleaned_data(df, output_file_path):
    df.to_csv(output_file_path, index=False)
    print(f"Cleaned dataset saved to {output_file_path}")

# Analysis: Top users
def top_users(df):
    top_users_df = df['username'].value_counts().head(3)
    return top_users_df

# Analysis: Average likes and retweets
def average_likes_and_retweets(df):
    avg_likes = df['likes'].mean()
    avg_retweets = df['retweets'].mean()
    return avg_likes, avg_retweets

# Analysis: Unique hashtags
def unique_hashtags(df):
    unique_hashtags_set = set()
    df['hashtags'].str.split(',').apply(lambda x: unique_hashtags_set.update([hashtag.strip() for hashtag in x if hashtag.strip()]))
    return len(unique_hashtags_set)

# Main function to run the data processing and analysis
def main():
    file_path = 'social_media_dataset.csv'  # Path to your dataset
    output_file_path = 'cleaned_social_media_dataset.csv'  # Output cleaned dataset path
    
    df = loadnexplore_data(file_path)
    df = handle_missing_values(df)
    df = correct_dt(df)
    df = remove_duplicates(df)
    df = clean_fields(df)
    save_cleaned_data(df, output_file_path)
    
    print("\nTop Users:")
    print(top_users(df))
    
    avg_likes, avg_retweets = average_likes_and_retweets(df)
    print(f"\nAverage Likes: {avg_likes:.2f}, Average Retweets: {avg_retweets:.2f}")
    
    print("\nNumber of Unique Hashtags:", unique_hashtags(df))

# Run the main function
if __name__ == "__main__":
    main()
