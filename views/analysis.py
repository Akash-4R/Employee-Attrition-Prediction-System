import streamlit as st
import matplotlib
import plotly.express as px
import pandas as pd   
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title="Analysis Dashboard", layout="wide")
def load_view():
    df = pd.read_csv('turnover.csv')
    # st.dataframe(df)

    # MAIN PAGE
    st.title(':bar_chart: Data Visualisation')
    st.markdown("##")
    avg_satisfy = round(df['satisfaction_level'].mean(), 2)
    avg_lastEval = round(df['last_evaluation'].mean(), 2)
    avg_numProj = int(df['number_project'].mean())
    print(avg_satisfy, avg_lastEval, avg_numProj)

    left_col, middle_col, right_col = st.columns(3, gap='medium)
    with left_col:
        st.subheader("Average Satisfaction Level : ")
        st.subheader(f"{avg_satisfy}")
    with middle_col:
        st.subheader("Average Last Evaluation : ")
        st.subheader(f"{avg_lastEval}")
    with right_col:
        st.subheader("Average Number of Projects : ")
        st.subheader(f"{avg_numProj}")
    
    st.markdown('---')
    font = { "color": "white", "size": 8 }

    # Graph 1
    fig1  = plt.figure(figsize=(3,3), facecolor="black")
    sns.countplot(x='number_project', data=df, hue="left")
    plt.title('Employee Attrition Vs Project Volume', color="white", fontsize=9)
    plt.xlabel("No of Projects", fontdict=font)
    plt.ylabel("Count", fontdict=font)
    plt.xticks(fontsize=6, color="white")
    plt.yticks(fontsize=6, color="white")
    #st.pyplot(fig1, use_container_width=False)

    # Graph 2
    fig2 = plt.figure(figsize=(3,3), facecolor="black")
    sns.countplot(x='salary', data=df, hue="left")
    plt.title('Employee Turnover by Salary', color="white", fontsize=9)
    plt.xlabel("Salary", fontdict=font)
    plt.ylabel("Count", fontdict=font)
    plt.xticks(fontsize=6, color="white")
    plt.yticks(fontsize=6, color="white")
    #st.pyplot(fig2, use_container_width=False)

    # sns.set(style="whitegrid")

    # Create the boxplot - Graph 3
    fig3 = plt.figure(figsize=(3,3), facecolor="black")
    sns.boxplot(x='left', y='satisfaction_level', data=df, hue='left', palette="Set1")
    # plt.rcParams['figure.figsize'] = [4, 4]
    plt.xlabel('Left', fontdict=font)
    plt.ylabel('Satisfaction Level', fontdict=font)
    plt.xticks(fontsize=6, color="white")
    plt.yticks(fontsize=6, color="white")
    plt.title('Satisfaction Level by Left Status',color="white", fontsize=9)
    # st.pyplot(fig3)

    # Graph 4
    fig4 = plt.figure(figsize=(3,3), facecolor="black")
    sns.histplot(x='satisfaction_level', data=df, hue="salary")
    plt.title('Children',color="white", fontsize=9)
    plt.xlabel("Satisfaction_level", fontdict=font)
    plt.ylabel("Count", fontdict=font)
    plt.xticks(fontsize=6, color="white")
    plt.yticks(fontsize=6, color="white")
    plt.legend(['low', 'medium', 'high'],title="Salary", fontsize='7', title_fontsize='7')

    lc, rc = st.columns(2)
    lc.pyplot(fig2, use_container_width=False)
    rc.pyplot(fig1, use_container_width=False)

    lc, rc = st.columns(2)
    lc.pyplot(fig3, use_container_width=False)
    rc.pyplot(fig4, use_container_width=False)
