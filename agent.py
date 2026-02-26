# agent.py

import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from config import MODEL_NAME, MAX_NEW_TOKENS, TEMPERATURE
from tools import calculator, get_weather


@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        device_map="auto",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )

    return pipe


pipe = load_model()

SYSTEM_PROMPT = """
You are a smart AI agent.

RULES:
- If math question → respond exactly:
  TOOL: calculator | expression=<expression>

- If weather question → respond exactly:
  TOOL: get_weather | city=<city>

- Otherwise answer normally.
"""


def call_llm(user_input: str) -> str:
    prompt = f"<s>[INST] {SYSTEM_PROMPT}\nUser: {user_input} [/INST]"

    output = pipe(
        prompt,
        max_new_tokens=MAX_NEW_TOKENS,
        temperature=TEMPERATURE,
        do_sample=True,
    )[0]["generated_text"]

    return output.split("[/INST]")[-1].strip()


def run_agent(user_input: str) -> str:
    llm_output = call_llm(user_input)

    # 🔥 Tool routing
    if llm_output.startswith("TOOL:"):
        try:
            tool_part = llm_output.replace("TOOL:", "").strip()
            name, params = tool_part.split("|")
            name = name.strip()

            key, value = params.split("=")
            value = value.strip()

            if name == "calculator":
                return calculator(value)

            if name == "get_weather":
                return get_weather(value)

        except Exception as e:
            return f"⚠️ Tool parsing error: {e}"

    return llm_output