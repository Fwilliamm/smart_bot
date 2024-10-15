import streamlit as st
def generate_response(user_input):
    # Logique de réponse avec un style ancien
    if "bonjour" in user_input.lower():
        return "Salut à toi, noble voyageur ! Comment puis-je te servir en ce jour ?"
    elif "comment ça va" in user_input.lower():
        return "Ma foi, je me porte bien, et toi, mon cher ami ?"
    elif "quel est ton nom" in user_input.lower():
        return "Je suis un humble serviteur des anciens, un messager des temps oubliés."
    else:
        return "Je crains que mes savoirs ne soient limités. Peut-être puis-je t'aider d'une autre manière ?"


def save_history(user_input, bot_response):
    with open("historique.txt", "a") as f:
        f.write(f"Vous : {user_input}\n")
        f.write(f"Bot : {bot_response}\n\n")    


st.title("Chatbot avec Streamlit")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Go')

if submit_button and user_input:
    response = generate_response(user_input)
    # Ajouter l'entrée utilisateur et la réponse à l'historique
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))
    save_history(user_input, response)

# Affichage de l'historique des échanges
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")


