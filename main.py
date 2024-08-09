import pandas as pd
import streamlit as st
import seaborn as sns
import json
import joblib
import catboost
import io
from io import StringIO
#import test_data  # Импортируем модуль test_data.py 


st.header('Какая оценка у отзыва')

LOCAL_PATH = 'data/'
PATH_DATA = LOCAL_PATH + 'orders.feather'
PATH_SULITABLE_TEACHERS_DATA = LOCAL_PATH + 'suitable_teachers.feather'
PATH_TEACHERS_DATA = LOCAL_PATH + 'orders.feather'
PATH_OUTPUT = 'output/'

PATH_UNIQUE_VALUES = 'data/unique_values.json'
PATH_MODEL = "models/cat_model.sav"

@st.cache_data
def load_data_csv(path):
    """Load data from path"""
    data = pd.read_csv(path)#, encoding='Windows-1251')
    # для демонстрации
    #data = data.sample(5000)
    return data

@st.cache_data
def load_data_feather(path):
    """Load data from path"""
    data = pd.read_feather(path)#, encoding='Windows-1251')
    return data

#@st.cache_data
uploaded_file = st.file_uploader("Загрузите файл для тестирования orders.csv", 
                                 type='csv', accept_multiple_files=False)
if uploaded_file is None:
    # Значение по умолчанию, которое будет использовано, пока файл не будет загружен
    orders_test = pd.read_csv(LOCAL_PATH + 'orders_test.csv')
else:
# To read file as scv:
    orders_test = load_data_csv(uploaded_file)
# Вызываем функцию обработки данных
    orders_test = test_data.prepare_test_orders(orders_test)
    st.dataframe(orders_test, height= 300)

@st.cache_data
def load_model(path):
    """Load model from path"""
    model = joblib.load(path)
    return model

