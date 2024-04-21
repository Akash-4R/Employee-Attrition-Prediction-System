import pandas as pd
import streamlit as st
import pickle

def highlight_row(row):
    if row['prediction'] == 1:
        return ['background-color: red'] * len(row)
    else:
        return ['background-color: green'] * len(row)

def load_view():
    uploaded_file = st.file_uploader("Insert file")
    if uploaded_file is not None:
        filename = uploaded_file.name
        df = pd.read_csv(uploaded_file)
        df.rename(columns={'sales': 'department', 'time_spend_company': 'experience_yrs'}, inplace=True)
        dept_encoding = {'IT': 0, 'RandD': 1, 'accounting': 2, 'hr': 3, 'management': 4, 'marketing': 5, 'product_mng': 6, 'sales': 7, 'support': 8, 'technical': 9}
        sal_encoding = {'low': 0, 'medium': 1, 'high': 2}
        df['salary'] = df['salary'].map(sal_encoding)
        df['department'] = df['department'].map(dept_encoding)
        df = df[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'Work_accident', 'promotion_last_5years', 'salary', 'department', 'experience_yrs']]
        load_model = pickle.load(open('views/attrition_model.sav', 'rb'))
        df['prediction'] = load_model.predict(df)
        styled_df = df.style.apply(highlight_row, axis=1)
        st.write(styled_df)
