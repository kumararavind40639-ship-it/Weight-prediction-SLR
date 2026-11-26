
# 📏 Height and Weight Predictor Using Machine Learning

## 📌 Project Overview

The **Height and Weight Predictor** is a Machine Learning project that uses **Simple Linear Regression (SLR)** to predict a person's weight based on their height.

The model is trained using a dataset and learns the relationship between height and weight. Based on the trained model, users can enter their height through a simple web interface and get a predicted weight.

This project demonstrates the practical implementation of Machine Learning using Python along with a user-friendly frontend developed using HTML and CSS.

## 🚀 Technologies Used

- **Python** – Programming language
- **Machine Learning** – Predictive modeling
- **Simple Linear Regression (SLR)** – Machine Learning algorithm
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Scikit-learn** – Model training and prediction
- **HTML** – Frontend structure
- **CSS** – Frontend styling
- **Pickle** – Saving and loading the trained ML model

## ⚙️ Project Workflow

1. **Dataset Collection:** Collect height and weight data.
2. **Data Preprocessing:** Load and prepare the dataset using Pandas.
3. **Model Training:** Train the model using Simple Linear Regression.
4. **Model Testing:** Evaluate the trained model using test data.
5. **Model Saving:** Save the trained model using Pickle.
6. **Frontend Development:** Create a user interface using HTML and CSS.
7. **Prediction:** Enter a height and get the predicted weight.

## 🧠 Machine Learning Algorithm

This project uses **Simple Linear Regression**, a supervised machine learning algorithm.

The algorithm identifies the linear relationship between two variables:

- **Independent Variable (X):** Height
- **Dependent Variable (Y):** Weight

### Linear Regression Equation

\[
Y = mX + C
\]

Where:
- Y = Predicted Weight
- X = Height
- m = Slope
- C = Intercept

## 💻 Features

- Predicts weight based on user-entered height.
- Uses Simple Linear Regression.
- Trained machine learning model.
- Model saved and loaded using Pickle.
- Simple and user-friendly web interface.
- HTML and CSS-based frontend.

## 📂 Project Structure

```text
Height-Weight-Predictor/
│
├── dataset.csv
├── train_model.py
├── model.pkl
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

*Note: Update the file names and folders according to your actual project structure.*

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Height-Weight-Predictor
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy scikit-learn flask
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

Open the local URL displayed in your terminal (usually):

```text
http://127.0.0.1:5000/
```

Enter your height and click the prediction button to see the estimated weight.

## 🎯 Project Objective

The main objective of this project is to understand how Simple Linear Regression works in Machine Learning and how a trained model can be integrated with a web application to make real-time predictions.

## 🔮 Future Improvements

- Improve prediction accuracy using larger datasets.
- Add graphical data visualization.
- Develop a responsive user interface.
- Experiment with other Machine Learning algorithms.
- Deploy the application online.

## 👨‍💻 Author

**Aravind Kumar**

B.Tech – Computer Science and Engineering

Interested in Machine Learning, Data Science, and Generative AI.

---

⭐ If you find this project interesting, don't forget to star the repository!
