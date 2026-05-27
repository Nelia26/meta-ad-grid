import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Meta Ads Grid", layout="wide")

# ---------- 1. БЕЗПЕЧНЕ ЗАВАНТАЖЕННЯ ДАНИХ ----------
DATA_PATH = Path(__file__).parent / "data.json"

if not DATA_PATH.exists():
    st.error("❌ data.json не знайдено. Перевір GitHub репозиторій.")
    st.stop()

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

rows = data.get("rows", [])

if not isinstance(rows, list):
    st.error("❌ Невірний формат JSON: 'rows' має бути списком")
    st.stop()

# ---------- 2. СТРУКТУРА ----------
st.title("📊 Рекламна сітка Meta Ads")

stages = {
    "awareness": [],
    "consideration": [],
    "conversion": [],
    "retention": []
}

# ---------- 3. ГРУПУВАННЯ (СТАБІЛЬНЕ) ----------
for row in rows:
    if not isinstance(row, dict):
        continue

    stage = str(row.get("stage", "unknown")).lower().strip()

    if stage in stages:
        stages[stage].append(row)

# ---------- 4. UI ----------
for stage_name, items in stages.items():
    st.subheader(stage_name.upper())

    if not items:
        st.caption("Немає сценаріїв")
        continue

    for item in items:
        with st.container():
            st.markdown("### 📌 Сценарій")

            st.write("🎯 Аудиторія:", item.get("audience", "-"))
            st.write("🎨 Креатив:", item.get("creative", "-"))
            st.write("⚙️ Подія:", item.get("optimization_event", "-"))
            st.write("📊 KPI:", item.get("kpi", "-"))

            st.divider()
