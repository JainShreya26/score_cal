import streamlit as st
import pandas as pd

# Define the dictionaries
dict1 = {
    "I1": None,
    "I3": 14604.2655217088,
    "I5": 7054.5304592156,
    "I7": 3863.9254651196,
    "I9": 2351.5101530719,
    "I11": 1175.7550765359,
    "I13": 587.8775382680,
    "I15": 293.9387691340,
    "I17": 138.5640646055,
    "I19": 1972.8239301891,
    "I21": 39.1918358845,
    "I23": 19.5959179423,
    "I25": 9.7979589711,
    "I27": 5.3665631460,
    "I29": 2.8685486624,
    "I31": 1.3856406461,
    "I33": 0.8164965809,
    "I35": 0.4082482905,
    "I37": 0.2041241452,
    "I39": 0.1166423687,
    "I41": 0.0583211844,
    "I43": 0.0268231465,
    "I45": 0.0134115733,
    "I47": 0.0067057866,
    "I49": 0.0036729106,
    "I51": 0.0022354458,
    "I53": 0.0011177229,
    "I55": 0.0004998609,
    "I57": 0.0002634498,
    "I59": 0.0001328053,
    "I61": 0.0000702706,
    "I63": 0.0000421208
}

dict2 = {
    "I1": 17280.0000000000,
    "I3": 10326.7751846492,
    "I5": 4988.3063257984,
    "I7": 3154.8819312298,
    "I9": 1662.7687752661,
    "I11": 831.3843876331,
    "I13": 415.6921938165,
    "I15": 195.9591794227,
    "I17": 100.8201660500,
    "I19": 54.8198631091,
    "I21": 27.7128129211,
    "I23": 13.8564064606,
    "I25": 6.9282032303,
    "I27": 4.0567404227,
    "I29": 1.9595917942,
    "I31": 1.0954451150,
    "I33": 0.5773502692,
    "I35": 0.2886751346,
    "I37": 0.1543033500,
    "I39": 0.0824786099,
    "I41": 0.0395519617,
    "I43": 0.0189668288,
    "I45": 0.0094834144,
    "I47": 0.0047417072,
    "I49": 0.0029990421,
    "I51": 0.0015806989,
    "I53": 0.0007069100,
    "I55": 0.0003725743,
    "I57": 0.0001916879,
    "I59": 0.0000953197,
    "I61": 0.0000500696,
    "I63": None
}

# Define a function to get the value based on the option and question id
def get_score_for_data(df):
    # Get the last row
    last_row = df.iloc[-1]

    option = last_row['Option']
    question = last_row['Question']
    if option == 1:
        return dict1.get(question, None)
    elif option == 2:
        return dict2.get(question, None)
    else:
        return None

# Streamlit app
st.title("Score Calculator")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    final_score = get_score_for_data(df)
    
    if final_score is not None and final_score != 0:
        # Calculate the inverse of the final score
        inverse_score = 1 / final_score
    else:
        inverse_score = None
    
    st.markdown(
        f"""
        <div style="border:2px solid #4CAF50; padding: 20px; margin: 20px; text-align: center;">
            <h2 style="color: #4CAF50;">The final k value is:</h2>
            <h1 style="font-size: 50px; color: #FF5733;">{final_score}</h1>
            <h2 style="color: #4CAF50;">The final ED50 value is:</h2>
            <h1 style="font-size: 50px; color: #FF5733;">{inverse_score if inverse_score is not None else 'Undefined'}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Please upload a CSV file.")
