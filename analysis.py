import pandas as pd

# Load the survey data
survey_data = pd.read_csv('data/survey_data.csv')

# Summary statistics
summary_stats = survey_data.describe()

# Calculate mode for categorical variables
mode_values = survey_data.mode().iloc[0]

# Calculate correlation matrix
# Exclude non-numeric columns before calculating correlation matrix
numeric_columns = survey_data.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = survey_data[numeric_columns].corr()


# Grouping and summarizing data
grouped_data = survey_data.groupby(['Education']).agg({'Age': 'mean', 'Question1': 'mean', 'Question2': 'mean'})

# Generating insights
# Example insights:
# 1. Average age of respondents with different levels of education
# 2. Average responses to specific questions based on education level
# 3. Correlation between age and responses to certain questions

print("Grouped and summarized data:")
print(grouped_data)
