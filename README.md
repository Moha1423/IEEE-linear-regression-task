# IEEE-linear-regression-task
## README.md

### Problem Statement
The goal of this project is to implement a **Linear Regression Model** from scratch using **Gradient Descent** to predict **Salary** based on **Years of Experience**. We aim to:
1. Minimize the Mean Squared Error (MSE) between the predicted and actual salaries.
2. Use Gradient Descent to optimize the model parameters (slope `m` and intercept `b`).
3. Visualize the optimization process and the cost function.

### Instructions on How to Run the Code

1. **Install Python & Libraries**:  
   The libraries needed are:
   pandas  , numpy , matplotlib
  

2. **Download Dataset**:  
   The dataset contains two columns:
   - `YearsExperience`: The number of years of work experience.
   - `Salary`: The salary of individuals based on their experience.

3. **Run the Code**:
   Open the Jupyter notebook and run each cell in sequence. The notebook is divided into the following sections:
   - **Importing Libraries**: Necessary imports (`pandas`, `numpy`, `matplotlib`).
   - **Loading the Dataset**: Load the salary dataset and display the first few rows.
   - **Mean Squared Error**: Function to compute the MSE between actual and predicted salaries.
   - **Gradient Descent Algorithm**: Function to update `m` and `b` to minimize the MSE.
   - **Training the Model**: Optimize `m` and `b` using Gradient Descent.
   - **Making Predictions**: Predict salary values using the optimized model.
   - **Plotting the Results**: Visualize the actual vs predicted salaries and the cost function.

  

4. **Visualizing Results**:  
   The model will plot:
   - A **scatter plot** of the actual salary values.
   - A **line plot** of the predicted salary values based on the optimized linear regression model.
   - A **3D plot** of the Mean Squared Error as a function of slope (`m`) and intercept (`b`).

### Approach

1. **Loading the Dataset**:  
   We begin by loading the dataset into a pandas DataFrame. The data contains two columns: `YearsExperience` and `Salary`. This forms the basis of our regression problem.

2. **Mean Squared Error (MSE)**:  
   The MSE is defined as the average of the squared differences between actual and predicted values. It's used to quantify the error between the predicted salary and the actual salary. We implemented the MSE function to compute this error, which will guide our optimization.

3. **Gradient Descent Algorithm**:  
   Gradient Descent is the iterative optimization algorithm used to find the best-fit line by minimizing the MSE. It updates the slope (`m`) and intercept (`b`) iteratively based on the gradients of the cost function (MSE) with respect to these parameters. The learning rate (`L`) controls the step size of each update.

4. **Training the Model**:  
   By running Gradient Descent for 1000 iterations, the model gradually converges to the optimal values for `m` (slope) and `b` (intercept) that minimize the MSE. This yields the best-fit line for salary prediction.

5. **Making Predictions**:  
   Once the optimal values for `m` and `b` are found, the model uses the equation `y = mx + b` to predict salary values for each value of `YearsExperience` in the dataset.

6. **Visualizing the Results**:  
   We plot the predicted salary values against the actual salary values to see how well the model performs. Additionally, we provide an optional 3D visualization of the MSE as a function of slope and intercept, giving insights into how the model optimizes these values.

### Repository Structure

```
├── Salary_Data.csv            # The dataset file with YearsExperience and Salary columns
├── notebook.ipynb             # Jupyter notebook containing the implementation
├── README.md                  # Instructions on how to run the code
```

### Key Features
- Custom implementation of **Gradient Descent** from scratch.
- Visualization of the optimization process and the resulting predictions.
- Compute and plot the cost function to evaluate model performance.

