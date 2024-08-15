
import pandas as pd
import re


#testie = "Бомбический аппарат за свои деньги!!! Память, скорость работы, съемка фото\видео, качество материалов корпуса, IP68. Все на высоте. Отличная альтернатива яблокам и самсунгам флагманского уровня. Недостатки за неделю работы пока не обнаружены. Рекомендую к покупке."
#test_df = pd.DataFrame([testie], columns=['Review'])
#print(test_df)
regex = re.compile("[А-ЯЁа-яёA-Za-z!\d]+")
#'only_text', 'len_review', 'num_exclamation_marks' - лучшие фичи для нашей модели. получим их.

def get_rus_words_only(row, regex=regex):
    return " ".join(regex.findall(row['Review']))
    

def get_len_review(row):
    len_r = len(row['only_text'].split())
    return  len_r



def get_num_exclamation_marks(row):
    num_exclamation_marks = row['only_text'].count('!')
    return  num_exclamation_marks


def get_prepared_test_df(test_df):
    test_df['only_text'] = test_df.apply(get_rus_words_only, axis = 1)
    test_df['len_review'] = test_df.apply(get_len_review, axis = 1)
    test_df['num_exclamation_marks'] = test_df.apply(get_num_exclamation_marks, axis = 1)
    test_df = test_df.drop('Review',axis = 1)
    return test_df

#
#prep_test = get_prepared_test_df(test_df)
#print(prep_test['only_text'])
#print(prep_test['len_review'])
#print(prep_test['num_exclamation_marks'])