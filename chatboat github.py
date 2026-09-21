import streamlit as st

from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI


# Page configuration
st.set_page_config(
    page_title="AI Text Assistant",
    page_icon="🤖"
)


# Title
st.title("AI Chatbot")
st.write("This chatbot is created by SSU University")
st.markdown("Hello! I'm your AI assistant. How can I assist you today?")


# Image
st.image(
    "https://img.freepik.com/premium-photo/young-girl-chatbot-chat-with-artificial-intelligence-1_765679-66.jpg?w=2000"
)


# Function to get API key
def get_api_key():

    if "api_key" not in st.session_state:
        st.session_state["api_key"] = ""

    api_key = st.text_input(
        "Enter your Google API Key:",
        type="password",
        key="api_key"
    )

    return api_key


# Get API key
api_key = get_api_key()


# Check API key
if not api_key:

    st.warning("Please enter your Google API Key to continue.")

else:

    # Create prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(
                "You are a helpful AI assistant. "
                "Please respond to user queries in English."
            ),

            MessagesPlaceholder(
                variable_name="chat_history"
            ),

            HumanMessagePromptTemplate.from_template(
                "{question}"
            ),
        ]
    )


    # Chat history
    msgs = StreamlitChatMessageHistory(
        key="langchain_messages"
    )


    # Google Gemini model
    model = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        google_api_key=api_key
    )


    # Chat input
    user_question = st.chat_input(
        "Ask me anything..."
    )


    # When user asks a question
    if user_question:

        # Display user message
        with st.chat_message("user"):
            st.write(user_question)


        # Display assistant response
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                try:

                    # Send question to Gemini
                    response = model.invoke(
                        prompt.format_messages(
                            chat_history=msgs.messages,
                            question=user_question
                        )
                    )


                    # Extract answer
                    if isinstance(response.content, list):

                        answer = "\n".join(
                            item.get("text", "")
                            for item in response.content
                            if isinstance(item, dict)
                            and item.get("type") == "text"
                        )

                    else:

                        answer = str(response.content)


                    # Show answer
                    st.markdown(answer)


                    # Save chat history
                    msgs.add_user_message(user_question)
                    msgs.add_ai_message(answer)


                except Exception as e:

                    st.error(
                        f"Error: {e}"
                    )

#cd C:\Users\pc streamlit run "StoryMotion AI.py"
#python -m streamlit run "C:\Users\pc\sem7.py"
# from langchain_core.prompts import (
#     ChatPromptTemplate,
#     HumanMessagePromptTemplate,
#     MessagesPlaceholder,
#     SystemMessagePromptTemplate,
# )

# from langchain_community.chat_message_histories import StreamlitChatMessageHistory
# from langchain_google_genai import ChatGoogleGenerativeAI

# import streamlit as st


# # PAGE CONFIGURATION

# st.set_page_config(
#     page_title="SSU AI Assistant",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # CUSTOM CSS

# st.markdown(
#     """
#     <style>

#     /* Main page */
#     .main {
#         padding-top: 1rem;
#     }

#     /* Main title */
#     .main-title {
#         text-align: center;
#         font-size: 42px;
#         font-weight: 700;
#         color: #4F46E5;
#         margin-bottom: 5px;
#     }

#     /* Subtitle */
#     .subtitle {
#         text-align: center;
#         color: #666666;
#         font-size: 18px;
#         margin-bottom: 5px;
#     }

#     /* University */
#     .university {
#         text-align: center;
#         color: #888888;
#         font-size: 14px;
#         margin-bottom: 25px;
#     }

#     /* Sidebar heading */
#     .sidebar-title {
#         text-align: center;
#         font-size: 25px;
#         font-weight: 700;
#         color: #4F46E5;
#     }

#     /* Info box */
#     .info-box {
#         background-color: #F5F3FF;
#         padding: 15px;
#         border-radius: 10px;
#         border-left: 4px solid #4F46E5;
#         margin-top: 15px;
#         margin-bottom: 15px;
#     }

#     /* Footer */
#     .footer {
#         text-align: center;
#         color: #888888;
#         font-size: 13px;
#         margin-top: 40px;
#         padding: 15px;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # HEADER

# st.markdown(
#     '<div class="main-title">🤖 SSU AI Assistant</div>',
#     unsafe_allow_html=True,
# )

# st.markdown(
#     '<div class="subtitle">Your Intelligent AI-Powered Chatbot</div>',
#     unsafe_allow_html=True,
# )

# st.markdown(
#     '<div class="university">🎓 Created for SSU University</div>',
#     unsafe_allow_html=True,
# )

# # IMAGE

# st.image(
#     "https://img.freepik.com/premium-photo/young-girl-chatbot-chat-with-artificial-intelligence-1_765679-66.jpg?w=2000",
#     width=500,
# )

# # SIDEBAR
# with st.sidebar:

#     st.markdown(
#         '<div class="sidebar-title">⚙️ Settings</div>',
#         unsafe_allow_html=True,
#     )

#     st.markdown("---")

#     # API KEY

#     st.subheader("🔑 Google Gemini API")

#     api_key = st.text_input(
#         "Enter your Google API Key",
#         type="password",
#         placeholder="Paste your API key here",
#     )

#     st.caption(
#         "🔒 Your API key is used only for this session."
#     )

#     st.markdown("---")

#     # CREATIVITY

#     st.subheader("🎚️ AI Creativity")

#     temperature = st.slider(
#         "Response creativity",
#         min_value=0.0,
#         max_value=1.0,
#         value=0.7,
#         step=0.1,
#         help="Higher values make responses more creative.",
#     )

#     st.markdown("---")

#     # ABOUT

#     st.subheader("ℹ️ About")

#     st.write(
#         """
#         **SSU AI Assistant** is an AI-powered chatbot
#         built using:

#         - 🐍 Python
#         - 🦜 LangChain
#         - 🤖 Google Gemini
#         - 🎈 Streamlit
#         """
#     )

#     st.markdown("---")

#     # FEATURES

#     st.subheader("✨ Features")

#     st.write("✅ AI Chat")
#     st.write("✅ Conversation Memory")
#     st.write("✅ Gemini AI")
#     st.write("✅ Custom Creativity")
#     st.write("✅ Clean Chat Interface")

#     st.markdown("---")

#     # CLEAR CHAT

#     clear_chat = st.button(
#         "🗑️ Clear Conversation",
#         use_container_width=True,
#     )

# # CHAT HISTORY

# msgs = StreamlitChatMessageHistory(
#     key="langchain_messages"
# )

# # CLEAR CHAT


# if clear_chat:

#     msgs.clear()

#     st.rerun()
# # API KEY CHECK

# if not api_key:

#     st.info(
#         "👈 Please enter your Google Gemini API key "
#         "in the sidebar to start chatting."
#     )

#     st.stop()

# # SYSTEM PROMPT


# prompt = ChatPromptTemplate(
#     messages=[

#         SystemMessagePromptTemplate.from_template(
#             """
#             You are SSU AI Assistant, a helpful, friendly,
#             intelligent and professional AI assistant.

#             Your job is to help students, teachers and users
#             with their questions.

#             Follow these rules:

#             1. Give clear and accurate answers.
#             2. Explain difficult concepts in simple language.
#             3. Use headings and bullet points when useful.
#             4. If the user asks for programming code,
#                provide properly formatted code.
#             5. If the user asks for an explanation,
#                provide examples when useful.
#             6. Be polite and professional.
#             7. Do not make up information.
#             8. If you are unsure about something,
#                clearly say that you are unsure.
#             9. Respond in English by default.
#             10. If the user asks for Hindi, Punjabi,
#                 or another language, respond in that language.

#             Keep answers relevant to the user's question.
#             """
#         ),

#         MessagesPlaceholder(
#             variable_name="chat_history"
#         ),

#         HumanMessagePromptTemplate.from_template(
#             "{question}"
#         ),
#     ]
# )

# # GEMINI MODEL
# try:

#     model = ChatGoogleGenerativeAI(
#         model="gemini-3.6-flash",
#         api_key=api_key,
#         temperature=temperature,
#     )

# except Exception as e:

#     st.error("❌ Unable to initialize Gemini.")

#     st.error(str(e))

#     st.stop()
# # WELCOME MESSAGE

# if len(msgs.messages) == 0:

#     with st.chat_message("assistant"):

#         st.markdown(
#             """
#             👋 **Hello! Welcome to SSU AI Assistant.**

#             I can help you with:

#             - 📚 Study questions
#             - 🐍 Python programming
#             - 💻 Coding problems
#             - 🧠 AI and Machine Learning
#             - 📝 Writing and explanations
#             - 💡 Ideas and brainstorming

#             **Ask me anything!**
#             """
#         )
# # DISPLAY PREVIOUS MESSAGES

# for message in msgs.messages:

#     if message.type == "human":

#         with st.chat_message("user"):

#             st.markdown(message.content)

#     elif message.type == "ai":

#         with st.chat_message("assistant"):

#             st.markdown(message.content)

# # CHAT INPUT

# user_question = st.chat_input(
#     "💬 Type your question here..."
# )

# # PROCESS USER QUESTION

# if user_question:

#     # USER MESSAGE
#     with st.chat_message("user"):

#         st.markdown(user_question)

#     with st.chat_message("assistant"):

#         with st.spinner("🤔 Thinking..."):

#             try:

#                 # Generate response
#                 response = model.invoke(
#                     prompt.format_messages(
#                         chat_history=msgs.messages,
#                         question=user_question,
#                     )
#                 )

#                 # EXTRACT RESPONSE TEXT
#                 if isinstance(response.content, list):

#                     answer = "\n".join(
#                         item.get("text", "")
#                         for item in response.content
#                         if isinstance(item, dict)
#                         and item.get("type") == "text"
#                     )

#                 else:

#                     answer = str(response.content)

#                 # DISPLAY RESPONSE

#                 if answer.strip():

#                     st.markdown(answer)

#                 else:

#                     st.warning(
#                         "⚠️ The AI returned an empty response."
#                     )

#                 # SAVE CHAT HISTORY
                
#                 msgs.add_user_message(
#                     user_question
#                 )

#                 msgs.add_ai_message(
#                     answer
#                 )


#             except Exception as e:

#                 st.error(
#                     "❌ Something went wrong while "
#                     "generating the response."
#                 )

#                 st.code(
#                     str(e)
#                 )



# # FOOTER

# st.markdown(
#     """
#     <div class="footer">
#         🤖 SSU AI Assistant |
#         Powered by Google Gemini + LangChain |
#         🎓 SSU University
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
