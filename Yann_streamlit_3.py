import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)


authenticator.login()


if st.session_state["authentication_status"]:
    st.title("Bienvenue")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')


# Importation du module
from streamlit_option_menu import option_menu

# Création du menu qui va afficher les choix qui se trouvent dans la variable options
with st.sidebar:

    st.write(f"Bienvenue {lesDonneesDesComptes['usernames']['root']['name']}")

    selection = option_menu(
                menu_title=None,
                options=["Accueil", "Photos"]
            )
    # Le bouton de déconnexion
    authenticator.logout("Déconnexion")

# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":

    st.write("Bienvenue sur ma page !")

    # affichage image accueil
    st.image("https://cdn-www.konbini.com/files/2024/03/messi-anatomie.jpg?width=3840&quality=75&format=webp")

# page Photo 
elif selection == "Photos":

    st.write("Bienvenue sur mon album photo")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Un chat")
        st.image("https://www.assuropoil.fr/wp-content/uploads/2023/07/avoir-un-chat-sante.jpg")

    with col2:
        st.header("Toujours un chat")
        st.image("https://www.peuple-animal.com/wp-content/uploads/2019/02/1739.800.jpg")

    with col3:
        st.header("Un autre chat")
        st.image("https://www.slate.fr/uploads/store/drupal_slate/chat_vener.jpg")
