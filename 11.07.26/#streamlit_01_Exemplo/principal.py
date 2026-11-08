import streamlit as st

# definição de paginas
page_00 = st.Page("pag_00.py", title="Pagina Inicial", )
page_01 = st.Page("pag_01.py", title="Pagina 01", )
page_02 = st.Page("pag_02.py", title="Pagina 02", )
page_03 = st.Page("pag_03.py", title="Pagina 03", )

# Setup navegação
pg = st.navigation([page_00, page_01, page_02, page_03])

pg.run()



