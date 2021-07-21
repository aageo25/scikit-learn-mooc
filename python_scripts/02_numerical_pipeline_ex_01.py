# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 📝 Exercise M1.03
#
# The goal of this exercise is to compare the generalization performance of our
# classifier (81% accuracy) to some baseline classifiers that would ignore the
# input data and instead make constant predictions.
#
# - What would be the score of a model that always predicts `' >50K'`?
# - What would be the score of a model that always predicts `' <=50K'`?
# - Is 81% or 82% accuracy a good score for this problem?
#
# Use a `DummyClassifier` and do a train-test split to evaluate
# its accuracy on the test set. This
# [link](https://scikit-learn.org/stable/modules/model_evaluation.html#dummy-estimators)
# shows a few examples of how to evaluate the generalization performance of these
# baseline models.

# %%
import pandas as pd

adult_census = pd.read_csv("../datasets/adult-census.csv")

# %% [markdown]
# We will first split our dataset to have the target separated from the data
# used to train our predictive model.

# %%
target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=target_name)

# %% [markdown]
# We start by selecting only the numerical columns as seen in the previous
# notebook.

# %%
numerical_columns = [
    "age", "capital-gain", "capital-loss", "hours-per-week"]

data_numeric = data[numerical_columns]

# %% [markdown]
# Split the dataset into a train and test sets.

# %%
from sklearn.model_selection import train_test_split

# Write your code here.


# %% [markdown]
# Use a `DummyClassifier` such that the resulting classifier will always
# predict the class `' >50K'`. What is the accuracy score on the test set?
# Repeat the experiment by always predicting the class `' <=50K'`.
#
# Hint: you can refer to the parameter `strategy` of the `DummyClassifier`
# to achieve the desired behaviour.

# %%
from sklearn.dummy import DummyClassifier

# Write your code here.
