# DSF 
Hugging face model on 10 variables:https://huggingface.co/spaces/iamomtiwari/Nutrition-Regression
Food Nutrition & Mental Health Analysis
This project demonstrates end-to-end data analytics and machine learning skills, starting from data preprocessing and visualization to regression modeling and evaluation. The objective was to explore the relationship between food nutrition and mental health indicators using a rich dataset sourced from Kaggle.

Project Overview
Phase 1: Data Acquisition & Preprocessing
Dataset: Food Nutrition dataset from Kaggle

Tools Used: Google Colab, Pandas, NumPy, Matplotlib, Seaborn

Steps:

Imported necessary Python libraries

Uploaded and loaded dataset using Pandas

Filtered numeric columns for statistical analysis

Identified and handled missing/null values

Dropped irrelevant columns (e.g., food)

Phase 2: Data Visualization
Used Matplotlib and Seaborn to understand patterns and relationships in the data:

Bar Chart: Visualized nutrient levels across food categories

Histogram: Explored caloric value distribution

Scatter Plot: Checked correlations between Caloric Value and Protein

Seaborn Plots: Provided enhanced visuals including bar plots, scatter plots, and histograms with better aesthetics and statistical summaries

Correlation Heatmap: Visualized strength of relationships between variables

Phase 3: Feature Scaling
Normalization (Min-Max Scaling): Rescaled data to [0, 1]

Standardization: Centered data using Z-score (mean = 0, std = 1)

Tools: MinMaxScaler, StandardScaler from Scikit-learn

Phase 4: Model Development & Training
Objective: Predict Nutrition Density (a continuous variable) using regression techniques

Tools: Scikit-learn, Train-Test Split

Preprocessing:

Dropped irrelevant features

Split data (80% training, 20% testing)

Models Implemented:
Support Vector Regressor (SVR)

MSE: 0.0034 | R²: ~1.0

Best performer – highly robust and accurate

Linear Regression

MSE: ~0.0 | R²: 1.0

Perfect fit, ideal for interpretability

Random Forest Regressor

MSE: 22.18 | R²: 0.9990

Excellent balance of accuracy and stability

Decision Tree Regressor

MSE: 141.96 | R²: 0.9937

Good performance, but prone to slight overfitting

K-Nearest Neighbors (KNN)

MSE: 1554.97 | R²: 0.9308

Underperformed due to high dimensionality issues

Key Highlights
Hands-on with exploratory data analysis (EDA) and visualization using Seaborn and Matplotlib

Applied both normalization and standardization to prepare data for modeling

Evaluated multiple regression algorithms with performance metrics like MSE and R²

Identified SVR and Linear Regression as top performers based on accuracy and simplicity

Skills Demonstrated
Data Analytics:
Data wrangling, filtering, cleaning

Exploratory visualizations and interpretation

Correlation analysis

Data Science:
Feature engineering

Normalization & standardization

Data splitting and preprocessing

Interpreting statistical outputs

Machine Learning:
Regression modeling with multiple algorithms

Performance evaluation (MSE, R²)

Model comparison and selection

![image](https://github.com/user-attachments/assets/8f3459ee-d6e3-41f5-9552-d2a63fbe59ae)


![image](https://github.com/user-attachments/assets/8de09aa5-292a-43fa-8187-9672a156a72b)


![image](https://github.com/user-attachments/assets/8fe0cc79-af89-4b4f-86f4-62c8051bb7a8)


![image](https://github.com/user-attachments/assets/d25b88b1-0648-4626-bedb-f8c5b1fbf59d)


![image](https://github.com/user-attachments/assets/e3609a3c-f50e-4027-b1b0-1e076fa1b87e)


![image](https://github.com/user-attachments/assets/4527df8e-616c-4b42-874e-b30ca8e1f28e)


![image](https://github.com/user-attachments/assets/1b5663b6-a670-43e3-a851-03cc14406c56)


![image](https://github.com/user-attachments/assets/b4ffea4e-5bce-4fbb-bb28-97c8abd8738b)


![image](https://github.com/user-attachments/assets/1a1a6752-8837-4975-a620-4ea0b0b356fb)


![image](https://github.com/user-attachments/assets/0fe905ac-997a-4d8d-91d6-4f03eae819e4)


![image](https://github.com/user-attachments/assets/c58a930a-7c17-4401-8671-7120c5f0a7b8)


