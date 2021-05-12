''' Lendo conjunto de dados'''

import pandas as pd
from pandas_datareader import data
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

gol_df=data.DataReader(name='GOLL4.SA',data_source='yahoo', start='2015-01-01')

st.write("""Visualização dos dados da companhia teste""")
gol_df
#gol_df.shape
#gol_df.Close
#gol_df.High



columns = st.multiselect(
        label='Qual gráfico deseja mostrar?', options=gol_df.columns)

st.line_chart(gol_df[columns])