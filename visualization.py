import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the survey data
survey_data = pd.read_csv('data/survey_data.csv')

# Visualizations
# Bar charts for categorical variables
categorical_columns = ['Gender', 'Education', 'Employment Status', 'Marital Status']
for column in categorical_columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(data=survey_data, x=column)
    plt.title(f'Bar Chart for {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Histograms for numerical variables
numerical_columns = ['Age', 'Question1', 'Question2', 'Question3', 'Question4', 'Question5',
                     'Question6', 'Question7', 'Question8', 'Question9', 'Question10']
for column in numerical_columns:
    plt.figure(figsize=(8, 6))
    plt.hist(survey_data[column], bins=10, color='skyblue', edgecolor='black')
    plt.title(f'Histogram for {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Pie chart for gender distribution
plt.figure(figsize=(8, 6))
survey_data['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen'])
plt.title('Gender Distribution')
plt.ylabel('')
plt.show()

# Correlation matrix heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
