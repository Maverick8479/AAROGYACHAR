import numpy as np
import pickle
import streamlit as st
import pandas as pd

df = pd.read_csv('disease_precaution.csv')
df = df.reset_index() 
dm = pd.read_csv('disease_medicine.csv')
dr = pd.read_csv('disease_riskFactors.csv')
dm = dm.reset_index()
dr = dr.reset_index()

loaded_model = pickle.load(open('model.pkl', 'rb'))
st.set_page_config(page_title = 'Disease Predictor')

hide_st_style = """
            <style>
           #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# creating a function for Prediction


def marks_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    return (prediction[0])

l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

l2 = {'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}

def main():
    # giving a title
    st.write('## Disease Prediction')
    st.write("")

    # getting the input data from the user

    col1, col2 = st.columns(2)
    with col1:
        s1   = st.selectbox('Symptom 1', l1)
    with col2:
        s2   = st.selectbox('Symptom 2', l1)
    with col1:
        s3   = st.selectbox('Symptom 3', l1)
    with col2:    
        s4   = st.selectbox('Symptom 4', l1)
    with col1:    
        s5   = st.selectbox('Symptom 5', l1)
    

    # code for Prediction
    #diagnosis = ''




    # creating a button for Prediction
    if st.button('Disease Prediction'):
        arr = np.zeros(132)


        for i, disease in enumerate(l1):
            if disease == s1:
                print(i)
                arr[i-1] = 1
            if disease == s2:
                print(i)
                arr[i-1] = 1
            if disease == s3:
                print(i)
                arr[i-1] = 1
            if disease == s4:
                print(i)
                arr[i-1] = 1
            if disease == s5:
                print(i)
                arr[i-1] = 1

        diagnosis = round(marks_prediction(arr))
        if diagnosis > 40 and diagnosis < 0:
            result = (f"**Cannot predict based on the data provided.**")
        else:
            d = list(l2.keys())[list(l2.values()).index(diagnosis)]
            result = (f"You have **{d}**")
            st.write("")
            st.error(result)
            st.write("")
            for index, row in df.iterrows():
                if row[1] == d:
                    st.write("**You should take the following precautions:**")
                    st.write(row[2:5])
                    break   

            
            for index, row in dr.iterrows():
                    if row[2] == d:
                        did = row[1]
                        for i, r in dm.iterrows():
                            if r[3] == did:
                                print(r[2])
                                st.write("**Commanly prescribed medicines:**")  
                                st.write("- " + r[2])   
                        break  



if __name__=='__main__':
    main()