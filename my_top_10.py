import streamlit as st
import os

def convert_stars_to_emoji(rating_str):
    """Convert rating string like '****' or '*** 1/2' to star emoji display."""
    rating_str = rating_str.strip()
    # Count full stars
    full_stars = rating_str.count('*')
    has_half = '1/2' in rating_str
    
    stars = '★' * full_stars
    if has_half:
        stars += '½'
    
    return stars

st.set_page_config(page_title="My 2025 Curated List - Top 5", layout="wide")

# Birthday greeting with floating animation
st.markdown("""
<style>
@keyframes bounce {
    0%, 100% { transform: translateY(0px) translateX(0px); opacity: 1; }
    25% { transform: translateY(-30px) translateX(10px); }
    50% { transform: translateY(-50px) translateX(-10px); }
    75% { transform: translateY(-30px) translateX(10px); }
}

.birthday-greeting {
    display: inline-block;
    font-size: 28px;
    font-weight: bold;
    color: #FF6B6B;
    animation: bounce 4s ease-in-out infinite;
    text-align: center;
    margin-bottom: 20px;
    width: 100%;
}
</style>
<div class="birthday-greeting">🎉 Alles Gute zum Geburtstag, Jig! 🎉</div>
""", unsafe_allow_html=True)

# Centered title and author's note
st.markdown("<h1 style='text-align: center;'> Top 5 Series & Movies of 2025</h1>", unsafe_allow_html=True)

# Author's note (English + German)
st.markdown(
    "<p style='text-align: center;'><b>English: Author's Note:</b> if you do not agree with any of this, I suggest you find sanity in oddity.</p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'><b>Deutschland: Anmerkung des Autors:</b> Wenn Sie mit nichts davon einverstanden sind, schlage ich vor, dass Sie in Kuriositäten Vernunft finden.</p>",
    unsafe_allow_html=True
)

# Define your data directly in the script (Top 5)
top_items = [
    {
        "title": "Pluribus",
        "rating": "**** 1/2",
        "kind": "Series",
        "source": "Apple TV",
        "img": "images/pluribus.jpg",
        "review": [
            "The only thing stopping it from hitting a 5 star level is that Carol Sturka actually needs to chill.",
            "I'm still trying to figure it out what Vince was thinking when he came up with the cast names. (Zosia, really?)",
        ],
    },
    {
        "title": "Frankenstein",
        "rating": "****",
        "kind": "Movie",
        "source": "",
        "img": "images/frankenstein.jpg",
        "review": [
            "An instant mind fucker, a delayed (almost impossible) hate towards the creature. Is this how God felt?",
            "Kein Problem!",
        ],
    },
    {
        "title": "Severance (Season 2)",
        "rating": "***1/2",
        "kind": "Series",
        "source": "Apple TV",
        "img": "images/severance_s2.jpg",
        "review": [
            "Chikhai Bardo and Cold Harbour are the major ships sailing through what may seem like a lonely boy trying to get over his ex.",
            "Please, I say please, cancel memories.",
        ],
    },
    {
        "title": "The Phoenician Scheme",
        "rating": "***",
        "kind": "Movie",
        "source": "",
        "img": "images/phoenician_scheme.jpg",
        "review": [
            "I guess I laugh at ubiquity. most often.",
            "To be in a scheme is to hate this movie.",
            "No drugs were harmed in filming and reviewing this movie. hahaha.",
        ],
    },
    {
        "title": "Common Side Effects",
        "rating": "***",
        "kind": "Series",
        "source": "Adult Swim",
        "img": "images/common_side_effects.jpg",
        "review": [
            "It rewards differently to think differently",
            "Common Side Effects? more like Common Side Quests.",
        ],
    },
]


# Render as a 3-column grid with image fallback
cols = st.columns(3)
for i, item in enumerate(top_items):
    with cols[i % 3]:
        img_path = item.get("img", "")
        if not img_path or not os.path.exists(img_path):
            img_path = "https://via.placeholder.com/400x225.png?text=No+Image"
        st.image(img_path, use_container_width=True)
        st.subheader(f"{i+1}. {item['title']}")
        star_display = convert_stars_to_emoji(item['rating'])
        st.caption(f"Kind: {item['kind']}  •  Source: {item['source']}  •  Rating: {star_display}")
        for line in item.get("review", []):
            st.write(f"- {line}")
        st.divider()

# Centered footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 24px;'><b>With Love,<br>Mtebeti</b></p>",
    unsafe_allow_html=True
)
