import pandas as pd
import streamlit as st

import json
import joblib
import catboost
import io
from io import StringIO
import test  # Импортируем модуль test.py 

LOCAL_PATH = 'data/'
PATH_DATA = LOCAL_PATH + 'orders.feather'
PATH_MODEL = "models/model_cb.pkl"

st.header('Какая оценка у отзыва о телефоне')

def load_model(path):
    """Load model from path"""
    model = joblib.load(path)
    return model
model = load_model(PATH_MODEL)



# Поле для ввода текста пользователем

user_input = st.text_input("Введите ваш отзыв в строку ниже и нажмите enter", '')
if user_input:  # Проверка, что строка не пустая
    st.write("Ваш отзыв: ")
    st.write( user_input)
     # Создание DataFrame
    test_df = pd.DataFrame([user_input], columns=['Review'])
    st.write("Лемматизированный отзыв:")
    #st.dataframe(test_df['Review'], heigh = 300)
    # Вызываем функцию обработки данных
    prep_test = test.get_prepared_test_df(test_df)
    st.write(prep_test['only_text'].iloc[0])

else:
    st.write("")


# Кнопка для запуска процесса цифровой оценки
if st.button('Узнать оценку'):
    if user_input:  # Проверка, что строка не пустая
        st.write("Предсказание оценки пользователя:")
        preds = model.predict(prep_test)
        st.write(preds[0])
    else:
        st.write("Пожалуйста, введите текст отзыва.")
