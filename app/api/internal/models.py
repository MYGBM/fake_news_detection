import pickle
import pandas as pd
from .preprocess import Preprocess

preprocess = Preprocess()

with open("assets/LR_model.pkl", "rb") as f:
    logistic_regression = pickle.load(f)
with open("assets/DT_model.pkl", "rb") as f:
    decision_tree = pickle.load(f)
with open("assets/RF_model.pkl", "rb") as f:
    random_forest = pickle.load(f)
with open("assets/GB_model.pkl", "rb") as f:
    gradient_boost = pickle.load(f)
with open("assets/vectorizer.pkl", "rb") as f:
    vectorize = pickle.load(f)


class Model:

    def __init__(self):
        self.logistic_regression = logistic_regression
        self.decision_tree = decision_tree
        self.random_forest = random_forest
        self.gradient_boost = gradient_boost
        self.vectorize = vectorize

    def output_label(self, x):
        return "Real" if x == 1 else "Fake"

    def predict(
        self,
        text: str,
    ) -> dict:
        text = [text]
        new_data_test = pd.DataFrame({"text": text})
        new_data_test["text"] = new_data_test["text"].apply(preprocess.preprocess_data)
        new_x_test = new_data_test["text"]
        new_xv_test = self.vectorize.transform(new_x_test)
        LR_prediction = self.logistic_regression.predict(new_xv_test)
        DT_prediction = self.decision_tree.predict(new_xv_test)
        RF_prediction = self.random_forest.predict(new_xv_test)
        GB_prediction = self.gradient_boost.predict(new_xv_test)

        return {
            "logistic_regression": self.output_label(LR_prediction),
            "decision_tree": self.output_label(DT_prediction),
            "random_forest": self.output_label(RF_prediction),
            "gradient_boosting": self.output_label(GB_prediction),
        }

    def predict_prob(
        self,
        text: str,
    ) -> dict:
        text = [text]
        new_data_test = pd.DataFrame({"text": text})
        new_data_test["text"] = new_data_test["text"].apply(preprocess.preprocess_data)
        new_x_test = new_data_test["text"]
        new_xv_test = self.vectorize.transform(new_x_test)
        LR_prediction = self.logistic_regression.predict_proba(new_xv_test)
        DT_prediction = self.decision_tree.predict_proba(new_xv_test)
        RF_prediction = self.random_forest.predict_proba(new_xv_test)
        GB_prediction = self.gradient_boost.predict_proba(new_xv_test)

        return {
            "logistic_regression": max(LR_prediction[0]),
            "decision_tree": max(DT_prediction[0]),
            "random_forest": max(RF_prediction[0]),
            "gradient_boosting": max(GB_prediction[0]),
        }
