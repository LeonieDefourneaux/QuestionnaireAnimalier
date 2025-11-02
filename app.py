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
        ["Vache", "Cheval", "Cochon", "Mouton", "Poule","Oie"],
        placeholder="Sélectionnez..."
    )
    # Question 3
with st.expander("3. Quels animaux de la savane vous fascinent le plus ?"):
    choix_savane = st.multiselect(
        "Choisissez une ou plusieurs options :",
        ["Lion", "Léopard", "Tigre", "Eléphant", "Phacochère", "Hyène"],
        placeholder="Sélectionnez..."
    )
with st.expander("4. Quels animaux de la forêt aimez-vous le plus ?"):
    choix_foret = st.multiselect(
        "Choisissez une ou plusieurs options :",
        ["Loups", "Ours", "Renard", "Ecureuil", "Cerf", "Moufette"],
        placeholder="Sélectionnez..."
    )
with st.expander("5. Quels animaux du désert affectionnez-vous le plus ?"):
    choix_desert= st.multiselect(
        "Choisissez une ou plusieurs options :",
        ["Mygale", "Fennec", "Serpent", "Chinchilla", "Chameau", "Suricate"],
        placeholder="Sélectionnez..."
    )


correspondances ={
    "Chien":9,
    "Chat":10,
    "Cochon d'Inde":10,
    "Poisson rouge":5,
    "Lapin":7,
    "Vache":6,
    "Cheval":9,
    "Cochon":3,
    "Mouton":8,
    "Poule":7,
    "Oie":3,
    "Lion":9,
    "Léopard":8,
    "Tigre":8,
    "Eléphant":8,
    "Phacochère":5,
    "Hyène":3,
    "Loups":9,
    "Ours":4,
    "Renard":8,
    "Ecureuil":8,
    "Cerf":7,
    "Moufette":7,
    "Mygale":0,
    "Fennec":10,
    "Serpent":3,
    "Chinchilla":9,
    "Chameau":4,
    "Suricate":9,
    
}




if st.button("Envoyer mes réponses"):
    st.subheader("Analyse de vos réponses :")

    grande_liste = choix_domestiques + choix_ferme + choix_savane + choix_foret + choix_desert
    nombre_animaux = len(grande_liste)
    scores_additionnes = 0
    for animaux in grande_liste:
        scores_additionnes += correspondances[animaux]
    st.write("Vous avez choisi", nombre_animaux, "animaux.")
    st.write("La somme des scores de vos animaux s'élève à ",scores_additionnes, ".")
    moyenne = scores_additionnes/nombre_animaux
    moyenne=round(moyenne,1)
    st.write("Votre moyenne de score est ",moyenne, ".")
    if "Chien" in grande_liste:
        st.write("Je vois que vous aimez bien les chiens. Vous voulez bien promener le mien ?")
    else:
        st.write("Ben alors, on aime pas les toutous?!")
