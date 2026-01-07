import streamlit as st
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Mediterranean Masala Crisps",
    page_icon="🌿",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(15px);}
    to {opacity: 1; transform: translateY(0);}
}

.fade-in {
    animation: fadeIn 1.2s ease-in;
}

.price {
    font-size: 28px;
    font-weight: bold;
    color: #1b5e20;
}

.buy-btn {
    background-color: #1b5e20;
    color: white;
    padding: 12px 22px;
    border-radius: 8px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HERO SECTION ------------------
st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align:center;'>Mediterranean Masala Crisps</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;font-size:18px;'>Where Indian warmth meets Mediterranean craft</p>",
    unsafe_allow_html=True
)
st.image("assets/lifestyle.jpg", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ------------------ STORY ------------------
st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
st.header("🌿 Why We Exist")
st.write("""
Snacking today is broken — too oily, too loud, too artificial.

Mediterranean Masala Crisps are baked flatbread crisps inspired by
Mediterranean techniques and Indian flavour intelligence.

Balanced. Addictive. Guilt-free.
""")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ------------------ PRODUCT SECTION ------------------
st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
st.header("🔥 Our First Product")

col1, col2 = st.columns([1, 1])

with col1:
    st.image("assets/product.png", use_container_width=True)

with col2:
    st.subheader("Smoked Paprika & Cumin")
    st.write("""
• Oven-baked artisan flatbread crisps  
• Mild heat, deep aroma  
• Designed for dips & spreads  
• No artificial flavours  
• Clean ingredient list  
""")

    st.markdown("<p class='price'>$3.99 / pack</p>", unsafe_allow_html=True)

    if st.button("🛒 Add to Cart"):
        with st.spinner("Adding to cart..."):
            time.sleep(1.2)
        st.success("Added to cart!")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ------------------ SOCIAL PROOF ------------------
st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
st.header("💬 Early Feedback")
st.write("""
⭐ “Feels premium without being intimidating”  
⭐ “Finally a chip that works with hummus”  
⭐ “Balanced spice — very repeatable”
""")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ------------------ FOOTER ------------------
st.markdown(
    "<p style='text-align:center;color:gray;'>© 2026 Mediterranean Masala Chips</p>",
    unsafe_allow_html=True
)
