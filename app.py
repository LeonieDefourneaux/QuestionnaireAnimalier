import streamlit as st

st.title("🐾 Aimez-vous les mêmes animaux que moi ?")
st.write("Merci de répondre aux questions ci-dessous :")
# Question 1
with st.expander("1. Quel type d'animaux domestiques préférez-vous ?"):
    choix_domestiques = st.multiselect(
        "Choisissez zéro, une, ou plusieurs options :",
        ["Chien", "Chat", "Cochon d'Inde", "Poisson rouge", "Lapin"],
        placeholder="Sélectionnez..."
    )
    # Question 2
with st.expander("2. Quels animaux de la ferme appréciez-vous le plus ?"):
    choix_ferme = st.multiselect(
        "Choisisse zéro, une, ou plusieurs options :",
        ["Vache", "Cheval", "Cochon", "Mouton", "Poule","Oie"],
        placeholder="Sélectionnez..."
    )
    # Question 3
with st.expander("3. Quels animaux de la savane vous fascinent le plus ?"):
    choix_savane = st.multiselect(
        "Choisissez zéro, une, ou plusieurs options :",
        ["Lion", "Léopard", "Tigre", "Eléphant", "Phacochère", "Hyène"],
        placeholder="Sélectionnez..."
    )
with st.expander("4. Quels animaux de la forêt aimez-vous le plus ?"):
    choix_foret = st.multiselect(
        "Choisissez zéro, une, ou plusieurs options :",
        ["Loups", "Ours", "Renard", "Ecureuil", "Cerf", "Moufette"],
        placeholder="Sélectionnez..."
    )
with st.expander("5. Quels animaux du désert affectionnez-vous le plus ?"):
    choix_desert= st.multiselect(
        "Choisissez zéro, une, ou plusieurs options :",
        ["Mygale", "Fennec", "Serpent", "Chinchilla", "Chameau", "Suricate"],
        placeholder="Sélectionnez..."
    )


correspondances ={
    "Chien":9,
    "Chat":10,
    "Cochon d'Inde":10,
    "Poisson rouge":4,
    "Lapin":10,
    "Vache":4,
    "Cheval":9,
    "Cochon":2,
    "Mouton":8,
    "Poule":7,
    "Oie":3,
    "Lion":9,
    "Léopard":8,
    "Tigre":8,
    "Eléphant":8,
    "Phacochère":2,
    "Hyène":1,
    "Loups":9,
    "Ours":3,
    "Renard":8,
    "Ecureuil":8,
    "Cerf":7,
    "Moufette":7,
    "Mygale":0,
    "Fennec":10,
    "Serpent":1,
    "Chinchilla":9,
    "Chameau":4,
    "Suricate":9,
    
}




if st.button("Envoyer mes réponses"):
    st.subheader("Analyse de vos réponses :")

    grande_liste = choix_domestiques + choix_ferme + choix_savane + choix_foret + choix_desert
    nombre_animaux = len(grande_liste)
    if nombre_animaux == 0:
        st.warning("Vous n’avez choisi aucun animal, ça ne peut pas marcher 😅")
    scores_additionnes = 0
    for animaux in grande_liste:
        scores_additionnes += correspondances[animaux]
    moyenne = scores_additionnes/nombre_animaux
    moyenne=round(moyenne,1)
    st.write("La moyenne des ",nombre_animaux," animaux que vous avez choisis est de ",moyenne, "/10.")
    if moyenne >9:
        st.write("Oh! On a tellement les mêmes goûts qu'on dirait que c'est moi qui ai coché les animaux!")
    elif moyenne > 8:
        st.write("Oh ! On a presque les mêmes goûts !")
    elif moyenne > 7:
        st.write("On a beaucoup de goûts en commun !")
    elif moyenne > 6:
        st.write("Il y a quelques animaux qu'on aime en commun :)")
    elif moyenne > 5:
        st.write("On a pas vraiment les mêmes goûts en termes d'animaux, mais c'est pas grave ;)")
    elif moyenne > 4:
        st.write("On a pas les mêmes goûts !")
    elif moyenne > 3:
        st.write("Vous avez des gouts différents des miens! Tant pis")
    elif moyenne > 2:
        st.write("Vous avez des gouts très différents des miens!")
    elif moyenne > 1:
        st.write("Vous aimez de drôles d'animaux...  Vous n'avez pas ça chez vous j'éspère ?")
    else:
        st.write("Houlàlà !!! Quels horribles animaux !")


    if "Mygale" in grande_liste:
        st.write("Vous aimez les mygales ?! Quelle affreuse bestiole")
    
    if "Chien" in grande_liste:
        st.write("Je vois que vous aimez bien les chiens. Vous voulez bien promener le mien ?")
    else:
        st.write("Ben alors, on aime pas les toutous?!")

    if "Hyène" in grande_liste:
        st.write("Ah vous aimez les hyènes ? Je vous vois bien rire comme elles !")
    

    
