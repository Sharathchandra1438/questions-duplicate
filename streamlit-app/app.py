import streamlit as st
import helper
import pickle

try:
    model = pickle.load(open('model.pkl','rb'))
except Exception:
    model = None

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    if model is not None:
        try:
            result = model.predict(query)[0]
            if result:
                st.header('Duplicate')
            else:
                st.header('Not Duplicate')
        except Exception as e:
            st.error(f"Model prediction failed: {e}")
    else:
        # fallback heuristic using fuzzy and longest-substr features
        try:
            fuzzy = helper.test_fetch_fuzzy_features(q1, q2)
            length_feats = helper.test_fetch_length_features(q1, q2)
            token_set_ratio = fuzzy[3]
            longest_substr_ratio = length_feats[2]
            score = (token_set_ratio / 100.0) * 0.7 + (longest_substr_ratio) * 0.3
            if score > 0.6:
                st.header('Duplicate (heuristic)')
            else:
                st.header('Not Duplicate (heuristic)')
            st.write({'score': score, 'token_set_ratio': token_set_ratio, 'longest_substr_ratio': longest_substr_ratio})
        except Exception as e:
            st.error(f"Heuristic failed: {e}")


