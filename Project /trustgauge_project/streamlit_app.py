import streamlit as st
from app.data_loader import load_data
from app.trust_score import calculate_trust_score

st.set_page_config(page_title="TrustGauge - Amazon Review Analyzer", layout="centered")

st.title("🛒 TrustGauge")
st.subheader("Amazon Product Reviews Analyzer")

product_name = st.text_input("Enter Product Name:")

if st.button("Analyze Trust Score"):
    if product_name:
        df = load_data()
        filtered = df[df['product_title'].str.contains(product_name, case=False, na=False)]
        reviews = filtered['review_body'].dropna().tolist()

        if not reviews:
            st.warning(f"No reviews found for '{product_name}'. Try another product.")
        else:
            score = calculate_trust_score(reviews)
            st.success(f"✅ Trust Score for '{product_name}': {score}%")
    else:
        st.error("Please enter a product name.")
