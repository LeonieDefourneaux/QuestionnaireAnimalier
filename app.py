import streamlit as st

st.title("🐾 Quels types d'animaux préférez-vous ?")
st.write("Merci de répondre aux questions ci-dessous :")
# Question 1
with st.expander("1. Quel type d'animaux domestiques préférez-vous ?"):
    choix_domestiques = st.multiselect(
        "Choisissez une ou plusieurs options :",
        ["Chien", "Chat", "Cochon d'Inde", "Poisson rouge", "Lapin"],
        placeholder="Sélectionnez..."
    )
    # Question 2
with st.expander("2. Quels animaux de la ferme appréciez-vous le plus ?"):
    choix_ferme = st.multiselect(
        "Choisissez une ou plusieurs options :",
        ["Vache", "Cheval", "Cochon", "Mouton", "Poule"],
        placeholder="Sélectionnez..."
    )
    # Question 3
with st.expander("3. Quels animaux de la savane vous fascinent le plus ?"):
    choix_sauvages = st.multiselect(
        "Choisissez une ou plusieurs options :",
        ["Lion", "Léopard", "Tigre", "Suricate", "Phacochère", "Hyène"],
        placeholder="Sélectionnez..."
    )
with st.expander("4. Quels animaux de la forêt aimez-vous le plus ?"):
    choix_foret = st.multiselect(
        "Choisissez une ou plusieurs options :",
        ["Loups", "Ours", "Renard", "Ecureuil", "Cerf", "Moufette"],
        placeholder="Sélectionnez..."
    )
if st.button("Envoyer mes réponses"):
    st.subheader("📋 Résumé de vos réponses :")
    st.write("Animaux domestiques :", choix_domestiques)
    st.write("Animaux de la ferme :", choix_ferme)
    st.write("Animaux sauvages :", choix_sauvages)