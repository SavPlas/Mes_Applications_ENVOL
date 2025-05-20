import streamlit as st
import base64  # Pour encoder les icônes si elles sont des images

st.set_page_config(page_title="Mes Applications", page_icon="🚀")

st.title("Mes Applications ENVOL")

search_term = st.text_input("Rechercher une application", "")

app_container = st.container()

# -----  Fonctions pour créer les éléments d'icône -----

def app_button(app_name, app_url, icon_path=None, icon_base64=None):
    """Crée un bouton qui ressemble à une icône d'application.

    Args:
        app_name (str): Le nom de l'application (affiché sous l'icône).
        app_url (str): L'URL à ouvrir lorsque le bouton est cliqué.
        icon_path (str, optional): Chemin vers une image d'icône locale. Defaults to None.
        icon_base64 (str, optional): Icône encodée en base64. Defaults to None.
    """

    col = st.columns(1)[0]  # Utilise une seule colonne pour chaque bouton (pour la mise en page)

    if icon_path:
        col.markdown(
            f"""
            <a href="{app_url}" target="_blank">
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 10px; cursor: pointer;">
                    <img src="{icon_path}" alt="{app_name}" style="width: 50px; height: 50px;">
                    <small style="margin-top: 5px;">{app_name}</small>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )
    elif icon_base64:
        col.markdown(
            f"""
            <a href="{app_url}" target="_blank">
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 10px; cursor: pointer;">
                    <img src="data:image/png;base64,{icon_base64}" alt="{app_name}" style="width: 50px; height: 50px;">
                    <small style="margin-top: 5px;">{app_name}</small>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )
    else:
        col.markdown(
            f"""
            <a href="{app_url}" target="_blank">
                <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 10px; cursor: pointer;">
                    <div style="width: 50px; height: 50px; background-color: #ddd; border-radius: 10px;"></div>
                    <small style="margin-top: 5px;">{app_name}</small>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )


# -----  Vos applications  -----

with app_container:
    cols = st.columns(3)  # Créer 3 colonnes pour 3 applications par ligne
    with cols[0]:
        app_button("ENVOL : toute l'école avec mes items de prédilection", "https://envoltoutelecole-h5e7hbqqr7uackudf85mer.streamlit.app", icon_path="https://img.icons8.com/color/50/school-building.png")
    with cols[1]:
        app_button("ENVOL : choix des classes", "https://scriptpy-gbbyvkv6cspksztny5mz5o.streamlit.app", icon_path="https://img.icons8.com/plasticine/50/classroom.png")
    with cols[2]:
        app_button("ENVOL : création d’un fichier avec items sélectionnées", "https://selectioncolonnespy-943nubrhrzjbbbf8mmcwks.streamlit.app", icon_path="https://img.icons8.com/color/50/document.png")
    with cols[2]:
        app_button("CHROMEBOOK : créationd'étiquette", "https://scriptpy-j8xsldmpuujezweetyasrs.streamlit.app", icon_path="https://img.icons8.com/color/50/document.png")

st.markdown("---")
st.caption("Applications approuvées")
