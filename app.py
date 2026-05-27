import streamlit as st
import json

# 1. ЧИТАЄМО ДАНІ
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

rows = data.get("rows", [])

# 2. СТРУКТУРА СІТКИ
groups = {
    "awareness": [],
    "consideration": [],
    "conversion": [],
    "retention": []
}

# 3. ГРУПУВАННЯ
for row in rows:
    stage = row.get("stage", "unknown")

    if isinstance(stage, str):
        stage = stage.lower().strip()
    else:
        stage = "unknown"

    if stage in groups:
        groups[stage].append(row)

# 4. UI
st.title("📊 Рекламна сітка Meta Ads")

for stage, items in groups.items():
    st.header(stage.upper())

    for item in items:
        st.markdown("### Сценарій")

        st.write("🎯 Аудиторія:", item.get("audience"))
        st.write("🎨 Креатив:", item.get("creative"))
        st.write("⚙️ Подія:", item.get("optimization_event"))
        st.write("📊 KPI:", item.get("kpi"))

        st.markdown("---")