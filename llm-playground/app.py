# LLM Playground/basic application where different LLMs response time will be measure
# Built and LLM benchmarking tool
# Author: Muhammad Humayun Khan

from dotenv import load_dotenv
import streamlit as st
from services.llm_factory import get_llm
from utils.timer import measure_time
import pandas as pd

load_dotenv()

# App title
st.title("LLM Playground")

# User Prompt
prompt = st.text_area("Enter your prompt")

providers = st.multiselect(
    "Select models to compare",
    ["gemini", "groq", "huggingface"],
    default=["gemini", "groq"]
)

# when button is clicked
if st.button("Compare Models"):

    if not prompt.strip():
        st.warning("Please enter a prompt.")

    elif not providers:
        st.warning("Please select at least one model.")

    else:
        results = []

        for provider in providers:
            try:
                llm = get_llm(provider)
                response, latency = measure_time(llm.invoke, prompt)

                results.append({
                    "model": provider,
                    "response": response.content,
                    "latency": latency
                })

            except Exception as e:
                results.append({
                    "model": provider,
                    "response": f"Error: {e}",
                    "latency": None
                })

        # model response
        st.subheader("Model Responses")

        for r in results:
            with st.expander(r["model"].upper()):
                st.write(r["response"])
                if r["latency"] is not None:
                    st.caption(f"{r['latency']} seconds")

        # Latency comparison
        latency_data = [
            {"Model": r["model"], "Response Time (sec)": r["latency"]}
            for r in results if r["latency"] is not None
        ]

        st.subheader("Latency Comparison")
        st.table(pd.DataFrame(latency_data))



