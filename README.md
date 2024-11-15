[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UDZuxCjG)
# **Social Media Data Analysis**

## Objective:
In this task, you'll work with a social media dataset containing user posts and related information. The goal is to clean the dataset so that it's usable for further analysis.

## Transformation steps
Preferably as functions.

1. **Importing and Initial Data Exploration**  
   - Load a dataset that contains columns: `user_id`, `username`, `message`, `date`, `likes`, `retweets`, `hashtags`.
   - Read the dataset into a Pandas DataFrame. You can inspect its structure using methods like `.info()`, `.head()`, etc.

2. **Handling Missing Values**  
   - Check if there are any empty values (`NaN`) in the dataset.
   - Handle the missing values by filling in a suitable default value.

3. **Correcting Data Types**  
   - Ensure that each column has the correct data type (e.g., dates as `DateTime`, numeric values as integers or floats).
   - Convert columns to the correct data types if necessary.

4. **Removing Duplicates**  
   - Check for duplicates in the dataset and remove them if found.

5. **Cleaning Text Fields** 
   - Clean the `message` field by removing extra spaces, special characters, or any irrelevant data.

6. **Saving the Cleaned Dataset**
   - After cleaning, save the dataset to a new CSV file.

## Analysis steps
Build **three** functions for data analysis based on the cleaned dataset. These must be called and the returned value from the functions printed out when progam is run.

1. **Top users**  
   -    top_users: Build code to identify and return the three users who posted the most messages.
  
2. **Average likes and retweets**  
   -    average_likes_and_retweets: Calculate and return the average number of likes and retweets per post.
  
3. **Unique hashtags**
   -    unique_hashtags: Determine and return the number of unique hashtags are present in the dataset.



