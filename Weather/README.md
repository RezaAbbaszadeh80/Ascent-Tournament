# Weather Prediction using Naive Bayes Classifier

This project aims to predict weather conditions using a Naive Bayes classifier algorithm. The input data is stored in the train.csv file. After training the model, it predicts the weather and saves the output in a CSV file.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies.

bash
pip install pandas==1.4.4

## Approach

1. Data Preparation:
   - The data is loaded from the train.csv file.
   - Data preprocessing steps such as handling missing values are performed.
   - A "month" column is created for the data.

2. Data Encoding:
   - The data is encoded, excluding the "month" column, to convert categorical variables into numeric form.

3. Model Training:
   - The Naive Bayes classifier algorithm is used to train the model.

4. Prediction and Evaluation:
   - The trained model is used to predict the weather conditions.
   - The accuracy of the model is evaluated by comparing the predictions with the data in the test.csv file.
   - The results are saved in an output file.

## Model Selection

To choose the Naive Bayes model, a pipeline was created and SVM, K-NN, and Naive Bayes methods were tested. Based on the accuracy of the results, the Naive Bayes model was selected.

Evaluation of the Model:

- Comparison between Naive Bayes and data_main:
   Number of equal values: 172
   Number of unequal values: 29

- Comparison between SVM and data_main:
   Number of equal values: 172
   Number of unequal values: 29

- Comparison between K-NN and data_main:
   Number of equal values: 172
   Number of unequal values: 29

Since the Naive Bayes model showed the same results as the other methods, it was chosen for the weather prediction.

## Usage

1. Prepare the data:
   - Ensure you have the train.csv file with the input data.
   - Optionally, check for missing values and handle them if needed.

2. Install dependencies:
   - Use the provided pip command to install the required version of pandas.

3. Run the code:
   - Execute the code to train the model, predict the weather, and evaluate the results.

4. Output:
   - The predicted weather results will be saved in an output file.

## Contribution

Contributions to this project are welcome. Feel free to open issues or submit pull requests to improve the code.

## collaborators

- **Reza Abbaszadeh**: https://github.com/RezaAbbaszadeh80
- **Elham Hosseini**: https://github.com/EliFaveen
