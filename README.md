# 🌸 Iris Flower Classifier API

This project is a simple and beginner-friendly **machine learning web API** that classifies flowers from the famous **Iris dataset**. It's built using **TensorFlow**, deployed with **Flask**, and tested using **Postman**.

## 🚀 What It Does

You can send information about a flower (like its petal and sepal measurements), and the API will tell you which type of Iris it is — **Setosa**, **Versicolor**, or **Virginica**.

It’s like asking a botanist for help… but digital!

---

## 🧠 How It Works

* The model was trained using **TensorFlow**, a popular tool for machine learning.
* It learned to classify flowers by looking at patterns in sepal and petal sizes.
* Once trained, we saved the model and used it inside a web service so others can use it too.

---

## 🌐 How It’s Deployed (with Flask)

* We wrapped the model into a **Flask** application.
* Flask creates a small website (a "server") that listens for flower data.
* When you send a flower’s measurements, Flask feeds it to the model and returns the prediction.
---

## 🧪 How It’s Tested (with Postman)

* We used **Postman**, a user-friendly tool that lets us test the API without needing to write extra code.
* Using Postman, we send flower data (like a virtual form submission).
* The API responds instantly with the flower type.
* This helps us confirm that everything is working as expected.

Example:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response:

```json
{
  "prediction": "Iris-setosa"
}
```

<img width="655" alt="Screenshot 2025-05-19 at 11 40 30 AM" src="https://github.com/user-attachments/assets/289c9ed3-21de-4985-be4f-05ca632de72d" />


---

## ✅ Summary

* ✔️ Built using TensorFlow (for machine learning)
* ✔️ Deployed with Flask (to create a web API)
* ✔️ Tested using Postman (to simulate real usage)




