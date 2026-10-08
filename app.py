import streamlit as st

from prompt_template import build_prompt
from llm import generate_response


st.set_page_config(
    page_title="Prompt Engineering App",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 Prompt Engineering App")

st.write(
    "Explore different prompting techniques using an LLM."
)



st.sidebar.header("⚙️ LLM Settings")


temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)


max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=100,
    max_value=1000,
    value=500,
    step=50
)


technique = st.selectbox(
    "Select Prompting Technique",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)



task = st.text_area(
    "Enter your task",
    placeholder="Example: Explain Artificial Intelligence in simple words.",
    height=150
)



if st.button("🚀 Generate Answer"):

    if not task.strip():

        st.warning(
            "⚠️ Please enter a task before generating the answer."
        )

    else:

        with st.spinner("🤖 Generating response..."):

            try:

                # Create prompt
                prompt = build_prompt(
                    technique,
                    task
                )

                # Generate LLM response
                response = generate_response(
                    prompt,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

                # Display answer
                st.subheader("✨ Generated Answer")

                st.write(response)


                # Display prompt
                with st.expander("🔍 View Generated Prompt"):

                    st.code(
                        prompt,
                        language="text"
                    )


                # Display settings
                st.info(
                    f"Technique: {technique}  |  "
                    f"Temperature: {temperature}  |  "
                    f"Max Tokens: {max_tokens}"
                )


            except Exception as e:

                st.error(
                    f"❌ Error while generating response: {e}"
                )


st.divider()

st.caption(
    "Prompt Engineering Demo | "
    "Zero-shot • One-shot • Few-shot • CoT • Manual CoT • ToT"
)