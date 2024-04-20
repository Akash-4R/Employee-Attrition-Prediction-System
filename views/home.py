import streamlit as st
import pandas as pd
import pickle

def load_view():
    page_bg_img = """
    <style>
    [data-testid = 'stAppViewContainer'] {
    background-image: url("https://img.freepik.com/premium-photo/top-view-wood-office-desk-table-flat-lay-workspace_35380-2854.jpg");
    background-size: cover;
    }

    [data-testid = 'stHeader'] {
    background-color: rgba(0, 0, 0, 0);
    }

    [data-testid = 'stSidebarContent'] {
    background-color: #17101E;
    width: 0.25wh;
    }

    [data-testid = 'stSidebarUserContent'] {
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
    st.sidebar.markdown("# Survey")

    satisfaction = st.sidebar.slider("### Satisfaction Level", min_value=0.0, max_value=1.0, value=0.01)
    evaluation = st.sidebar.slider("### Last Evaluation", min_value=0.0, max_value=1.0, value=0.01)
    projectCount = st.sidebar.slider("### Number of Projects", min_value=1, max_value=7, value=1)
    averageMonthlyHours = st.sidebar.slider("### Average Monthly Working Hours", min_value=96, max_value=310, value=1)
    experience_yrs = st.sidebar.slider("### Years of Experience", min_value=2, max_value=10, value=1)
    workAccident = st.sidebar.slider("### Work Accident", min_value=0, max_value=1, value=1)
    promotion = st.sidebar.slider("### Promotion in the last 5 years", min_value=0, max_value=1, value=1)

    dept_options = ['sales',
                    'technical',     
                    'support',    
                    'IT',      
                    'product_mng',
                    'marketing',  
                    'RandD',         
                    'accounting',    
                    'hr',            
                    'management'
                    ]

    salary_options = ["low", "medium", "high"]
    selected_dept = st.sidebar.selectbox("### Departament:", dept_options)
    selected_salary = st.sidebar.selectbox("### Salary", salary_options)

    user_input = {
        'satisfaction_level': satisfaction,
        'last_evaluation': evaluation,
        'number_project': projectCount,
        'average_montly_hours': averageMonthlyHours,
        'Work_accident': workAccident,
        'promotion_last_5years': promotion,
        'salary': selected_salary,
        'department': selected_dept,
        'experience_yrs' : experience_yrs
    }

    # st.sidebar.write(user_input)

    dept_encoding = {'IT': 0, 'RandD': 1, 'accounting': 2, 'hr': 3, 'management': 4, 'marketing': 5, 'product_mng': 6, 'sales': 7, 'support': 8, 'technical': 9}
    sal_encoding = {'low': 0, 'medium': 1, 'high': 2}
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False

    def click_button():
        st.session_state.clicked = True

    st.sidebar.button('Submit', on_click=click_button)

    if st.session_state.clicked:
        user_input['department'] = dept_encoding[user_input['department']]
        user_input['salary'] = sal_encoding[user_input['salary']]
        input_df = pd.DataFrame(user_input, index = [0])
        load_model = pickle.load(open('views/attrition_model.sav', 'rb'))
        y_pred = load_model.predict(input_df)
        if y_pred == 1:
            st.write("Employee is expected to leave")
        else:
            st.write("Safe")
        st.session_state.clicked = False


        
