''' Lendo conjunto de dados'''

import pandas as pd
from pandas_datareader import data
import streamlit as st

gol_df=data.DataReader(name='GOLL4.SA',data_source='yahoo', start='2015-01-01')

st.title("""Visualização dos dados da companhia TESTE""")
gol_df
#gol_df.shape
#gol_df.Close
#gol_df.High



columns = st.multiselect(
        label='Qual gráfico deseja mostrar?', options=gol_df.columns)

st.line_chart(gol_df[columns])
