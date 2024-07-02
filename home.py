import streamlit as st
import pandas as pd
import pickle

def load_view():
    page_bg_img = """
    <style>
    [data-testid = 'stAppViewContainer'] {
    background-image: url("https://i.pinimg.com/originals/0e/29/f9/0e29f9d0e7f62100d528f74f12c0a7e9.jpg");
    background-size: cover;
    }

    [data-testid = 'stHeader'] {
    background-color: rgba(0, 0, 0, 0);
    }

    [data-testid = 'tContent'] {
    background-color: #17101E;
    width: 0.25wh;
    }

    [data-testid = 'tUserContent'] {
    padding: 3rem 1.5rem;
    color: #F6F3F9;
    }

    [data-testid = 'stMarkdownContainer'] {
    color: #F6F3F9;
    }

    [data-testid = 'stWidgetLabel'] {
    padding: 3px 0px;
    font-size: 16px;
    }

    [data-testid = 'stThumbValue'] {
    color: #945BCD;
    }

    [data-testid = 'stButton'] {
    display: flex;
    justify-content: center;
    }
    
    .st-emotion-cache-1vzeuhh {
    background-color: #5B83CD;
    }

    [data-testid = 'baseButton-secondary'] {
    background-color: #7DA6F1;
    width: 10rem

    }

    .st-emotion-cache-10fz3ls {
    color: #000000; 
    font-size: 40px;
    }

    # .st-ef{
    #       background-color:   rgb(11, 100, 100);
    # }

    # .css-demzbm {
    #       background-color:   rgb(11, 100, 100);
    # }

    # div.stSlider > div > div[class = "st-ag st-ah st-ai st-aj st-ak st-al st-am"] >div  {
    #   background: linear-gradient(to right, #82CFD0 0%, #82CFD0 50%, #fff 50%, #fff 100%);
    #   border: solid 1px #82CFD0;
    #   border-radius: 8px;
    #   outline: none;


    #   transition: background 450ms ease-in;
    #   -webkit-appearance: none;
    # }

    # div.css-1inwz65.e88czh80{      background-color:   rgb(250, 250, 250);  
    # color:   rgb(250, 250, 250);!important
    # }

    # div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div {
    #     background: rgb(1 1 1 / 0%); } 


    # div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    #     background-color: rgb(14, 38, 74); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} 

        
    # div.stSlider > div[data-baseweb="slider"] > div > div > div > div
    #                                 { color: rgb(14, 38, 74); }
        
    # div.stSlider > div[data-baseweb = "slider"] > div > div {{
    #     background: rgb(1, 183, 158); }}

    h1 {
    color: #F6F3F9;
    }

    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title("Employee Attrition Prediction System")
    st.write("Employee attrition poses significant challenges to businesses by disrupting operations and increasing recruitment costs. To address this, the Employee Attrition Prediction System leverages data analytics to identify patterns and predict future turnover. This system collects and analyzes employee data, including demographics, performance, and satisfaction, to uncover attrition drivers and forecast at-risk employees. By providing actionable insights, EAMS helps organizations formulate effective retention strategies, ultimately reducing turnover, enhancing employee engagement, and optimizing operational efficiency. The result is a more stable, motivated workforce and cost savings from improved retention")
    with st.form("Survey"):
        satisfaction = st.slider("### Employee Satisfaction Level", min_value=0.0, max_value=10.0, value=0.00)
        evaluation = st.slider("### Last Evaluation of Employer", min_value=0.0, max_value=10.0, value=0.00)
        projectCount = st.number_input("### Number of Projects", min_value=1, max_value=7, value=1,step=1)
        averageMonthlyHours = st.slider("### Average Monthly Working Hours", min_value=96, max_value=310, value=96)
        experience_yrs = st.number_input("### Years of Experience", min_value=2, max_value=10, value=2,step=1)
        workAccident = st.radio("### Occurence of Work Accidents",["Yes","No"])
        promotion = st.radio("### Promotion in the last 5 years",["Yes","No"])

        dept_options = ['Sales',
                        'Technical',     
                        'Support',    
                        'IT',      
                        'Product Management',
                        'Marketing',  
                        'RandD',         
                        'Accounting',    
                        'HR',            
                        'Management'
                        ]

        salary_options = ["Low", "Medium", "High"]
        selected_dept = st.selectbox("### Departament", dept_options)
        selected_salary = st.selectbox("### Employee Salary", salary_options)
        
        if 'clicked' not in st.session_state:
            st.session_state.clicked = False

        def click_button():
            st.session_state.clicked = True

        st.form_submit_button('Submit', on_click=click_button)

        if st.session_state.clicked:
            user_input = {
                'satisfaction_level': satisfaction/10,
                'last_evaluation': evaluation/10,
                'number_project': projectCount,
                'average_montly_hours': averageMonthlyHours,
                'Work_accident': 1 if workAccident=="Yes" else 0,
                'promotion_last_5years': 1 if promotion=="Yes" else 0,
                'salary': selected_salary,
                'department': selected_dept,
                'experience_yrs' : experience_yrs
            }
            dept_encoding = {'IT': 0, 'RandD': 1, 'Accounting': 2, 'HR': 3, 'Management': 4, 'Marketing': 5, 'Product Managment': 6, 'Sales': 7, 'Support': 8, 'Technical': 9}
            sal_encoding = {'Low': 0, 'Medium': 1, 'High': 2}
            user_input['department'] = dept_encoding[user_input['department']]
            user_input['salary'] = sal_encoding[user_input['salary']]
            input_df = pd.DataFrame(user_input, index = [0])
            load_model = pickle.load(open('views/attrition_model.sav', 'rb'))
            y_pred = load_model.predict(input_df)
            if y_pred == 1:
                #st.write("Employee is expected to leave")
                st.markdown("<h2 style='text-align: center; color: white;'>Employee is expected to leave the company</h2>", unsafe_allow_html=True)
            else:
                #st.write("Safe")
                st.markdown("<h2 style='text-align: center; color: white;'>Employee is expected to stay in the company</h2>", unsafe_allow_html=True)
            st.session_state.clicked = False
        