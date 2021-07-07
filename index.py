# SELECT id, post_name, post_type, post_author, post_date from wpvw_posts where post_type in ('page', 'post') and post_status = 'publish'

# Library
import pandas as pd

# Open CSV
df = pd.read_csv("wpvw_posts.csv",header=None)


# Add column name
df.columns = ['post_id','post_name','post_type','post_author','post_date']


# Select all duplicate rows based on one column
duplicateRowsDF = df[df.duplicated(['post_name'], keep=False)]

# Sort values
duplicateRowsDF =  duplicateRowsDF.sort_values(["post_name"],ascending = (True))

# Export CSV
duplicateRowsDF.to_csv('duplicates.csv', index=False)

