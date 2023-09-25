# Imports
import pandas as pd
import numpy as np
import streamlit as st

# Configurações iniciais
np.set_printoptions(suppress = True)
pd.set_option('display.float_format', '{:.2f}'.format)
st.set_page_config(layout = 'wide')

# Título
style_h1 = "<style>h1 {text-align: center}</style>"
st.markdown(style_h1, unsafe_allow_html = True)
st.title('Simulação do Faturamento')
st.write('')
st.write('')
st.write('')
st.write('')

# Funções

# carregamento dos dados
def load_data(file_path):
    
    df = pd.read_csv(file_path)

    return df

# aumento percentual
def aumento_percentual(df, aumento):
    
    resultado_faturamento = {
            'product_id': [],
            'faturamento_atual': [],
            'faturamento_aumentado':[],
            'ganho_faturamento':[],
            'faturamento_novo':[],
            'variacao_faturamento':[],
            'variacao_percentual':[]
        }

    for row in range(len(df)):
    
        preco_atual_medio = df['price_mean'][row]
        demanda_atual = df['quantity_mean'][row]*7

        preco_aumentado = preco_atual_medio*(1 + (aumento/100))
        aumento_demanda = (aumento/100)*df['price_elasticity_abs'][row]
        demanda_nova = demanda_atual/aumento_demanda

        faturamento_atual = round(preco_atual_medio*demanda_atual, 2)
        faturamento_novo = round(preco_aumentado*demanda_nova, 2)
        faturamento_aumentado = round(faturamento_atual*(1 + (aumento/100)), 2)
        ganho_faturamento = round(faturamento_aumentado - faturamento_atual, 2)
        variacao_faturamento = round(faturamento_novo - faturamento_atual, 2)
        variacao_percentual = round((100*((faturamento_novo - faturamento_atual)/faturamento_atual)), 2)

        resultado_faturamento['product_id'].append(df['product_id'][row])
        resultado_faturamento['faturamento_atual'].append(faturamento_atual)
        resultado_faturamento['faturamento_aumentado'].append(faturamento_aumentado)
        resultado_faturamento['ganho_faturamento'].append(ganho_faturamento)
        resultado_faturamento['faturamento_novo'].append(faturamento_novo)
        resultado_faturamento['variacao_faturamento'].append(variacao_faturamento)
        resultado_faturamento['variacao_percentual'].append(variacao_percentual)

    resultado = pd.DataFrame(resultado_faturamento).sort_values(by = 'variacao_percentual', ascending = False)
    resultado = resultado.reset_index(drop = True)
    
    return resultado

# redução percentual
def reducao_percentual(df, reducao):
    
    resultado_faturamento = {
            'product_id': [],
            'faturamento_atual': [],
            'faturamento_reduzido':[],
            'perda_faturamento':[],
            'faturamento_novo':[],
            'variacao_faturamento':[],
            'variacao_percentual':[]
        }

    for row in range(len(df)):
    
        preco_atual_medio = df['price_mean'][row]
        demanda_atual = df['quantity_mean'][row]*7

        preco_reduzido = preco_atual_medio*(1 - (reducao/100))
        aumento_demanda = (reducao/100)*df['price_elasticity_abs'][row]
        demanda_nova = demanda_atual*aumento_demanda

        faturamento_atual = round(preco_atual_medio*demanda_atual, 2)
        faturamento_novo = round(preco_reduzido*demanda_nova, 2)
        faturamento_reduzido = round(faturamento_atual*(1 - (reducao/100)), 2)
        perda_faturamento = round(faturamento_atual - faturamento_reduzido, 2)
        variacao_faturamento = round(faturamento_novo - faturamento_atual, 2)
        variacao_percentual = round((100*((faturamento_novo - faturamento_atual)/faturamento_atual)), 2)

        resultado_faturamento['product_id'].append(df['product_id'][row])
        resultado_faturamento['faturamento_atual'].append(faturamento_atual)
        resultado_faturamento['faturamento_reduzido'].append(faturamento_reduzido)
        resultado_faturamento['perda_faturamento'].append(perda_faturamento)
        resultado_faturamento['faturamento_novo'].append(faturamento_novo)
        resultado_faturamento['variacao_faturamento'].append(variacao_faturamento)
        resultado_faturamento['variacao_percentual'].append(variacao_percentual)

    resultado = pd.DataFrame(resultado_faturamento).sort_values(by = 'variacao_percentual', ascending = False)
    resultado = resultado.reset_index(drop = True)
    
    return resultado

# df resultante final
def simulation(df):

    # escolhendo entre aumento ou redução
    option = st.selectbox(
    'Escolha se o preço receberá um aumento ou uma redução: ',
    ('Aumento', 'Redução'))
    st.write('Você escolheu: ', option)
    st.write('')
    st.write('')

    # escolhendo o valor do aumento ou da redução percentual
    if option == 'Aumento':
        number = st.number_input("Digite o valor do aumento percentual: ")
        st.write('O aumento percentual é de: ', number)
        df = aumento_percentual(df, number)

    else:
        number = st.number_input("Digite o valor da redução percentual: ")
        st.write('A redução percentual é de: ', number)
        df = reducao_percentual(df, number)

    # mostrando o Dataframe Resultante
    st.write('')
    st.write('')
    st.dataframe(df, use_container_width = True)
        
    return df

# ETL
if __name__ == "__main__":
    file_path = 'archive/df_elasticidade_preco.csv'
    file_path_epc = 'archive/df_elasticidade_cruzada.csv'
    df = load_data(file_path)
    df_ep = load_data(file_path)
    df_epc = load_data(file_path_epc)
    result = simulation(df)

# Elasticidade de preço
st.write('')
st.write('')
st.header('Elasticidade de Preço')
st.dataframe(df_ep, use_container_width = True)

# Elasticidade de preço cruzada
st.write('')
st.write('')
st.header('Elasticidade de Preço Cruzada')
st.dataframe(df_epc, use_container_width = True)

# python -m streamlit run app.py