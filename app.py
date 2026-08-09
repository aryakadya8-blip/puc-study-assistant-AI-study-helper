import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="PUC Study Assistant",
    page_icon="📚"
)

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

st.title("📚 PUC Study Assistant")
st.write("Your personal AI study helper")

subject = st.selectbox(
    "📖 Choose Subject",
    ["Physics", "Chemistry", "Mathematics", "English"]
)

mode = st.selectbox(
    "🎯 Choose Mode",
    ["Doubt Solver", "Explain Topic", "Exam Notes", "Quiz"]
)

question = st.text_area(
    "✏️ Ask your question",
    placeholder="Example: Explain Newton's second law..."
)

if st.button("🤖 Ask AI", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        prompt = f"""
You are a friendly PUC Study Assistant.

Subject: {subject}
Mode: {mode}

Student question:
{question}

Give a clear answer suitable for a PUC student.

For numerical problems:
1. Give the formula.
2. Explain the symbols.
3. Substitute the values.
4. Show the calculation.
5. Give the final answer.

For theory:
- Explain simply.
- Give important points.
- Mention exam-important points.
"""

        with st.spinner("🤔 Thinking..."):
            response = client.responses.create(
                model="gpt-5-mini",
                input=prompt
            )

        st.subheader("📖 Answer")
        st.write(response.output_text)
