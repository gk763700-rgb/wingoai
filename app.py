import streamlit as st
import pandas as pd
from collections import Counter

st.set_page_config(
    page_title="Wingo AI Research Bot",
    page_icon="📊",
    layout="wide"
)

st.title("🎯 Wingo AI Research Bot")
st.caption("Historical Data Analysis & Statistics")

st.warning(
    "यह टूल केवल पुराने परिणामों का सांख्यिकीय विश्लेषण करता है। "
    "अगले परिणाम की गारंटी या निश्चित भविष्यवाणी नहीं करता।"
)

st.subheader("📥 Enter Previous Results")

data = st.text_area(
    "Enter numbers from 0 to 9, separated by commas",
    placeholder="1, 5, 3, 8, 2, 5, 0, 9"
)

if st.button("Analyze Results"):
    try:
        numbers = [
            int(x.strip())
            for x in data.split(",")
            if x.strip()
        ]

        if len(numbers) < 5:
            st.error("Please enter at least 5 results.")
        elif any(n < 0 or n > 9 for n in numbers):
            st.error("Only numbers from 0 to 9 are allowed.")
        else:
            counts = Counter(numbers)
            total = len(numbers)

            st.success(f"Total results: {total}")

            df = pd.DataFrame({
                "Number": list(range(10)),
                "Frequency": [counts[i] for i in range(10)]
            })

            df["Observed %"] = (
                df["Frequency"] / total * 100
            ).round(2)

            st.subheader("📊 Number Frequency")
            st.bar_chart(
                df.set_index("Number")["Frequency"]
            )

            st.dataframe(df, use_container_width=True)

            st.subheader("🔥 Most Frequent Numbers")
            st.write(
                df.sort_values(
                    "Frequency",
                    ascending=False
                ).head(3)
            )

            st.subheader("📈 Recent Results")
            st.write(numbers[-10:])

            st.info(
                "Past frequency does not establish "
                "the probability of the next result."
            )

    except ValueError:
