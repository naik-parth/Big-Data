import streamlit as st
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["amazon_reviews"]
collection = db["products"]

st.set_page_config(page_title="Product Score Lookup", page_icon="📦", layout="centered")
st.title("🔍 Amazon Product Score Lookup")

# --- Autocomplete Search Logic ---
typed_name = st.text_input("Type Product Name", "")
category = st.text_input("Enter Product Category", "")

suggestions = []
if typed_name:
    # Fetch up to 5 product name suggestions
    cursor = collection.find(
        {"product_title": {"$regex": f"^{typed_name}", "$options": "i"}},
        {"product_title": 1}
    ).limit(5)

    suggestions = [doc["product_title"] for doc in cursor]

if suggestions:
    selected_product = st.selectbox("Select Product", suggestions)
else:
    selected_product = None

# --- Search Button ---
if st.button("Get Product Score") and selected_product and category:
    result = collection.find_one({
        "product_title": selected_product,
        "product_category": category
    })

    if result:
        st.success(f"✅ Product Score: {result.get('product_score', 'N/A')}")
    else:
        st.warning("⚠️ No matching product found.")