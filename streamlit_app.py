import streamlit as st
import pandas as pd
from io import BytesIO
from converter import build_xml

st.title("Excel → MS Project XML Converter")

uploaded_file = st.file_uploader("Projektplan (Excel) hochladen", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    xml_tree = build_xml(df)
    
    xml_io = BytesIO()
    xml_tree.write(xml_io, encoding='utf-8', xml_declaration=True)
    
    st.success("Konvertierung erfolgreich!")
    st.download_button(
        label="MS Project XML herunterladen",
        data=xml_io.getvalue(),
        file_name="project.xml",
        mime="application/xml"
    )
