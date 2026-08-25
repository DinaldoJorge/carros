import streamlit as st
import pandas as pd
import os

# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================

st.set_page_config(
    page_title="AutoCadastro PRO",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CSS - TEMA MODERNO VERDE OLIVA
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

/* =====================================================
   FONTE
===================================================== */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}


/* =====================================================
   FUNDO PRINCIPAL
===================================================== */

.stApp {
    background: linear-gradient(
        135deg,
        #F4F3E8 0%,
        #E5E8D2 50%,
        #D8DEC0 100%
    );
}


/* =====================================================
   TEXTOS GERAIS
===================================================== */

.stApp p,
.stApp label,
.stApp span,
.stApp h1,
.stApp h2,
.stApp h3 {
    color: #26301D;
}


/* =====================================================
   SIDEBAR
===================================================== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #26301D,
        #3E4D2D
    );
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}


/* =====================================================
   HERO / BANNER
===================================================== */

.hero {
    background: linear-gradient(
        135deg,
        #3F4F2F,
        #6F803F
    );

    padding: 45px 30px;

    border-radius: 24px;

    text-align: center;

    margin-bottom: 25px;

    box-shadow:
        0 10px 30px rgba(38, 48, 29, 0.25);
}

.hero h1 {
    color: #FFFFFF !important;

    font-size: 48px;

    font-weight: 800;

    margin: 0;
}

.hero p {
    color: #F5F5E8 !important;

    font-size: 19px;

    font-weight: 500;

    margin-top: 10px;
}


/* =====================================================
   TÍTULO DAS PÁGINAS
===================================================== */

.titulo-pagina {
    color: #26301D !important;

    font-size: 34px;

    font-weight: 800;

    margin-bottom: 15px;
}


/* =====================================================
   TEXTO DE DESTAQUE
===================================================== */

.destaque {
    text-align: center;

    font-size: 22px;

    font-weight: 600;

    color: #39452A !important;

    margin-bottom: 35px;

    line-height: 1.7;
}

.destaque span {
    color: #60752E !important;

    font-weight: 800;
}


/* =====================================================
   LABELS DOS CAMPOS
===================================================== */

[data-testid="stWidgetLabel"] label,
.stTextInput label,
.stNumberInput label,
.stTextArea label,
.stSelectbox label {
    color: #26301D !important;

    font-size: 16px !important;

    font-weight: 700 !important;
}


/* =====================================================
   INPUTS
===================================================== */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;

    color: #26301D !important;

    font-size: 16px !important;

    font-weight: 500 !important;

    border: 2px solid #8A9861 !important;

    border-radius: 12px !important;
}


/* PLACEHOLDER */

.stTextInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #6B6B6B !important;
}


/* INPUT QUANDO CLICADO */

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border: 2px solid #556B2F !important;

    box-shadow:
        0 0 0 2px rgba(85, 107, 47, 0.15) !important;
}


/* =====================================================
   SELECTBOX
===================================================== */

[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;

    color: #26301D !important;

    border: 2px solid #8A9861 !important;

    border-radius: 12px !important;

    font-weight: 600 !important;
}

[data-baseweb="select"] span {
    color: #26301D !important;
}


/* =====================================================
   MÉTRICAS
===================================================== */

[data-testid="stMetric"] {
    background: #FFFFFF;

    padding: 25px;

    border-radius: 18px;

    border-left: 7px solid #667A36;

    box-shadow:
        0 8px 20px rgba(0, 0, 0, 0.08);
}

[data-testid="stMetricLabel"] {
    color: #4B5C2B !important;

    font-size: 16px !important;

    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: #26301D !important;

    font-size: 32px !important;

    font-weight: 800 !important;
}


/* =====================================================
   CARD PERSONALIZADO
===================================================== */

.card {
    background: #FFFFFF;

    color: #26301D !important;

    border-radius: 20px;

    padding: 30px;

    border: 1px solid #B8C18D;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.10);
}

.card h2,
.card h3,
.card p {
    color: #26301D !important;
}


/* =====================================================
   BOTÕES
===================================================== */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    width: 100%;

    min-height: 52px;

    background: linear-gradient(
        135deg,
        #556B2F,
        #748544
    ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    font-family: 'Poppins', sans-serif !important;

    font-size: 16px !important;

    font-weight: 700 !important;

    box-shadow:
        0 6px 16px rgba(85, 107, 47, 0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background: linear-gradient(
        135deg,
        #3F4F2F,
        #60752E
    ) !important;

    color: #FFFFFF !important;
}


/* =====================================================
   FORMULÁRIO
===================================================== */

[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.45);

    border: 1px solid #B8C18D;

    border-radius: 20px;

    padding: 25px;
}


/* =====================================================
   TABELA
===================================================== */

[data-testid="stDataFrame"] {
    background: #FFFFFF;

    border-radius: 15px;

    border: 1px solid #B8C18D;
}


/* =====================================================
   ALERTAS
===================================================== */

[data-testid="stAlert"] {
    color: #26301D !important;

    font-weight: 600;
}


/* =====================================================
   RODAPÉ
===================================================== */

.footer {
    text-align: center;

    color: #4B5C2B !important;

    margin-top: 50px;

    padding: 20px;

    font-size: 14px;

    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# ARQUIVO DE DADOS
# =====================================================

ARQUIVO = "carros.csv"


# =====================================================
# FUNÇÕES
# =====================================================

def carregar_dados():
    if os.path.exists(ARQUIVO):
        try:
            return pd.read_csv(ARQUIVO)
        except Exception:
            pass

    return pd.DataFrame(
        columns=[
            "Marca",
            "Modelo",
            "Ano",
            "Cor",
            "Placa",
            "Quilometragem",
            "Valor",
            "Observações"
        ]
    )


def salvar_dados(dados):
    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =====================================================
# CARREGAR DADOS
# =====================================================

df = carregar_dados()


# =====================================================
# MENU LATERAL
# =====================================================

st.sidebar.markdown("# 🚗 AutoCadastro")

st.sidebar.markdown(
    "### Gestão inteligente de veículos"
)

st.sidebar.divider()

menu = st.sidebar.radio(
    "MENU",
    [
        "🏠 Dashboard",
        "➕ Cadastrar Carro",
        "🚘 Carros Cadastrados"
    ]
)


# =====================================================
# DASHBOARD
# =====================================================

if menu == "🏠 Dashboard":

    st.markdown(
        """<div class="hero">
<h1>🚗 AutoCadastro PRO</h1>
<p>Gestão inteligente para seus veículos</p>
</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        """<div class="destaque">
<span>Organize.</span> Controle. Gerencie.
<br>
Todos os seus veículos em <span>um só lugar.</span>
</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        """<div class="titulo-pagina">
📊 Visão Geral
</div>""",
        unsafe_allow_html=True
    )

    total_carros = len(df)

    if df.empty:
        valor_total = 0.0
        km_total = 0
    else:
        df["Valor"] = pd.to_numeric(
            df["Valor"],
            errors="coerce"
        ).fillna(0)

        df["Quilometragem"] = pd.to_numeric(
            df["Quilometragem"],
            errors="coerce"
        ).fillna(0)

        valor_total = df["Valor"].sum()
        km_total = df["Quilometragem"].sum()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🚗 Veículos Cadastrados",
            total_carros
        )

    with col2:
        st.metric(
            "💰 Valor Total da Frota",
            f"R$ {valor_total:,.2f}"
        )

    with col3:
        st.metric(
            "🛣️ Quilometragem Total",
            f"{km_total:,.0f} km"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """<div class="card">
<h2>🚀 Seu controle começa aqui</h2>

<p>
Cadastre seus veículos, acompanhe informações importantes
e mantenha sua frota organizada de forma simples, rápida
e profissional.
</p>

</div>""",
        unsafe_allow_html=True
    )


# =====================================================
# CADASTRAR CARRO
# =====================================================

elif menu == "➕ Cadastrar Carro":

    st.markdown(
        """<div class="titulo-pagina">
➕ Novo Veículo
</div>""",
        unsafe_allow_html=True
    )

    st.markdown(
        """<div class="destaque">
Adicione um novo veículo ao seu
<span>AutoCadastro PRO.</span>
</div>""",
        unsafe_allow_html=True
    )

    with st.form("cadastro_carro", clear_on_submit=True):

        col1, col2 = st.columns(2)

        with col1:

            marca = st.text_input(
                "🏷️ Marca"
            )

            modelo = st.text_input(
                "🚗 Modelo"
            )

            ano = st.number_input(
                "📅 Ano",
                min_value=1900,
                max_value=2035,
                value=2020,
                step=1
            )

            cor = st.selectbox(
                "🎨 Cor",
                [
                    "Verde Oliva",
                    "Preto",
                    "Branco",
                    "Prata",
                    "Cinza",
                    "Vermelho",
                    "Azul",
                    "Amarelo",
                    "Outro"
                ]
            )

        with col2:

            placa = st.text_input(
                "🔢 Placa"
            )

            quilometragem = st.number_input(
                "🛣️ Quilometragem",
                min_value=0,
                value=0,
                step=1
            )

            valor = st.number_input(
                "💰 Valor do Veículo",
                min_value=0.0,
                value=0.0,
                step=1000.0
            )

            observacoes = st.text_area(
                "📝 Observações"
            )

        cadastrar = st.form_submit_button(
            "💾 Cadastrar Veículo"
        )

    if cadastrar:

        if marca.strip() and modelo.strip() and placa.strip():

            novo_carro = pd.DataFrame([
                {
                    "Marca": marca.strip(),
                    "Modelo": modelo.strip(),
                    "Ano": int(ano),
                    "Cor": cor,
                    "Placa": placa.strip().upper(),
                    "Quilometragem": int(quilometragem),
                    "Valor": float(valor),
                    "Observações": observacoes.strip()
                }
            ])

            df = pd.concat(
                [df, novo_carro],
                ignore_index=True
            )

            salvar_dados(df)

            st.success(
                "🚗 Veículo cadastrado com sucesso!"
            )

            st.rerun()

        else:

            st.warning(
                "⚠️ Preencha os campos Marca, Modelo e Placa."
            )


# =====================================================
# CARROS CADASTRADOS
# =====================================================

elif menu == "🚘 Carros Cadastrados":

    st.markdown(
        """<div class="titulo-pagina">
🚘 Minha Frota
</div>""",
        unsafe_allow_html=True
    )

    if df.empty:

        st.info(
            "🚗 Nenhum veículo cadastrado ainda."
        )

        st.markdown(
            """<div class="card">

<h3>🚀 Comece agora!</h3>

<p>
Vá até o menu <b>➕ Cadastrar Carro</b>
e adicione seu primeiro veículo.
</p>

</div>""",
            unsafe_allow_html=True
        )

    else:

        busca = st.text_input(
            "🔎 Pesquisar veículo",
            placeholder="Digite marca, modelo, placa ou cor"
        )

        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:
            df_filtrado = df

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("🗑️ Gerenciar Veículos")

        carro_excluir = st.selectbox(
            "Selecione um veículo para excluir",
            df.index,
            format_func=lambda indice:
                f"{df.loc[indice, 'Marca']} "
                f"{df.loc[indice, 'Modelo']} "
                f"— {df.loc[indice, 'Placa']}"
        )

        if st.button("🗑️ Excluir Veículo"):

            df = df.drop(carro_excluir)

            df = df.reset_index(drop=True)

            salvar_dados(df)

            st.success(
                "🚗 Veículo excluído com sucesso!"
            )

            st.rerun()


# =====================================================
# RODAPÉ
# =====================================================

st.markdown(
    """<div class="footer">
🚗 AutoCadastro PRO • Gestão inteligente de veículos
</div>""",
    unsafe_allow_html=True
)