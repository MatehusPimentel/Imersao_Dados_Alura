import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Customizado para melhorar a aparência ---
st.markdown("""
    <style>
    /* Estilo geral */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Título principal */
    h1 {
        color: #1f77b4;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Subtítulos */
    h2, h3 {
        color: #2c3e50;
        font-weight: 600;
    }
    
    /* Cards de métricas */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
    }
    
    /* Barra lateral com cor personalizada */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #c8c6af 0%, #b8b69f 100%);
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, #c8c6af 0%, #b8b69f 100%);
    }
    
    /* Estilo dos filtros */
    .filter-section {
        background: white;
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 4px solid #1f77b4;
    }
    
    .filter-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 0.8rem;
        font-size: 1.1rem;
        font-weight: 600;
        color: #2c3e50;
    }
    
    .filter-icon {
        font-size: 1.5rem;
    }
    
    /* Melhorar aparência dos multiselect */
    .stMultiSelect [data-baseweb="select"] {
        background-color: white;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
    
    .stMultiSelect [data-baseweb="select"]:hover {
        border-color: #1f77b4;
    }
    
    /* Badges de contagem */
    .filter-badge {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .info-box-title {
        font-size: 0.9rem;
        opacity: 0.9;
        margin-bottom: 0.3rem;
    }
    
    .info-box-value {
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    /* Botões customizados */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    /* Avisos */
    .stWarning {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 4px;
    }
    
    /* Tabela de dados */
    [data-testid="stDataFrame"] {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
    }
    
    /* Divisores */
    hr {
        margin: 2rem 0;
        border: none;
        border-top: 2px solid #e0e0e0;
    }
    
    /* Tooltips e informações */
    .tooltip-info {
        background-color: #e7f3ff;
        border-left: 4px solid #2196F3;
        padding: 0.75rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    /* Slider customizado */
    .stSlider [data-baseweb="slider"] {
        margin-top: 1rem;
    }
    
    /* Checkbox estilizado */
    .stCheckbox {
        padding: 0.5rem 0;
    }
    
    /* Expander customizado */
    .streamlit-expanderHeader {
        background-color: white;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        font-weight: 600;
    }
    
    /* Pills para tags */
    .filter-pill {
        display: inline-block;
        background-color: #e3f2fd;
        color: #1976d2;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        margin: 0.2rem;
        font-size: 0.85rem;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# --- Função para carregar dados com cache ---
@st.cache_data
def carregar_dados():
    """Carrega os dados com cache para melhor performance"""
    df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
    return df

# --- Carregamento dos dados ---
with st.spinner('🔄 Carregando dados...'):
    df = carregar_dados()

# --- Barra Lateral (Filtros) ---
with st.sidebar:
    # Logo/Header da sidebar
    st.markdown("""
        <div style="text-align: center; padding: 1rem 0 1.5rem 0;">
            <h2 style="margin: 0; color: #2c3e50;">🎯 Painel de Filtros</h2>
            <p style="margin: 0.5rem 0 0 0; color: #3d3d3d; font-size: 0.9rem;">
                Personalize sua análise
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Box de informação total de dados
    st.markdown(f"""
        <div class="info-box">
            <div class="info-box-title">📊 TOTAL DE REGISTROS</div>
            <div class="info-box-value">{len(df):,}</div>
        </div>
    """, unsafe_allow_html=True)
    
    # --- FILTRO DE ANO ---
    st.markdown("""
        <div class="filter-section">
            <div class="filter-header">
                <span class="filter-icon">📅</span>
                <span>Período Temporal</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    anos_disponiveis = sorted(df['ano'].unique())
    
    # Opção de selecionar todos os anos ou range
    modo_ano = st.radio(
        "Modo de seleção:",
        ["Todos os anos", "Selecionar específicos", "Intervalo"],
        key="modo_ano",
        label_visibility="collapsed"
    )
    
    if modo_ano == "Todos os anos":
        anos_selecionados = anos_disponiveis
        st.success(f"✅ {len(anos_selecionados)} anos selecionados")
    elif modo_ano == "Selecionar específicos":
        anos_selecionados = st.multiselect(
            "Escolha os anos",
            anos_disponiveis,
            default=anos_disponiveis,
            help="Selecione um ou mais anos específicos"
        )
        if anos_selecionados:
            st.markdown(f'<div class="filter-badge">📌 {len(anos_selecionados)} anos</div>', unsafe_allow_html=True)
    else:  # Intervalo
        col1, col2 = st.columns(2)
        with col1:
            ano_inicio = st.selectbox("De:", anos_disponiveis, index=0)
        with col2:
            ano_fim = st.selectbox("Até:", anos_disponiveis, index=len(anos_disponiveis)-1)
        anos_selecionados = [ano for ano in anos_disponiveis if ano_inicio <= ano <= ano_fim]
        st.info(f"📊 {len(anos_selecionados)} anos no intervalo")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FILTRO DE SENIORIDADE ---
    st.markdown("""
        <div class="filter-section">
            <div class="filter-header">
                <span class="filter-icon">👔</span>
                <span>Nível de Senioridade</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    senioridades_disponiveis = sorted(df['senioridade'].unique())
    
    # Opção rápida: todos ou seleção manual
    if st.checkbox("Selecionar todas as senioridades", value=True, key="todos_senioridade"):
        senioridades_selecionadas = senioridades_disponiveis
    else:
        senioridades_selecionadas = st.multiselect(
            "Níveis de experiência",
            senioridades_disponiveis,
            default=senioridades_disponiveis,
            help="Filtre por nível profissional"
        )
    
    # Mostrar seleção com pills
    if senioridades_selecionadas:
        st.markdown("**Selecionados:**")
        pills_html = "".join([f'<span class="filter-pill">{s}</span>' for s in senioridades_selecionadas])
        st.markdown(pills_html, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FILTRO DE CONTRATO ---
    st.markdown("""
        <div class="filter-section">
            <div class="filter-header">
                <span class="filter-icon">📝</span>
                <span>Tipo de Contratação</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    contratos_disponiveis = sorted(df['contrato'].unique())
    
    # Usar expander para economizar espaço
    with st.expander("Selecionar tipos de contrato", expanded=False):
        # Checkbox para cada tipo
        contratos_selecionados = []
        selecionar_todos_contratos = st.checkbox("Selecionar todos", value=True, key="todos_contratos")
        
        if selecionar_todos_contratos:
            contratos_selecionados = contratos_disponiveis
        else:
            for contrato in contratos_disponiveis:
                if st.checkbox(contrato, value=True, key=f"contrato_{contrato}"):
                    contratos_selecionados.append(contrato)
    
    st.markdown(f'<div class="filter-badge">✓ {len(contratos_selecionados)} tipos selecionados</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FILTRO DE TAMANHO DA EMPRESA ---
    st.markdown("""
        <div class="filter-section">
            <div class="filter-header">
                <span class="filter-icon">🏢</span>
                <span>Porte da Empresa</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
    
    # Radio buttons para seleção mais visual
    modo_tamanho = st.radio(
        "Selecione os portes:",
        ["Todos", "Customizar"],
        key="modo_tamanho",
        horizontal=True
    )
    
    if modo_tamanho == "Todos":
        tamanhos_selecionados = tamanhos_disponiveis
        st.success("✅ Todos os portes incluídos")
    else:
        tamanhos_selecionados = st.multiselect(
            "Escolha os tamanhos",
            tamanhos_disponiveis,
            default=tamanhos_disponiveis,
            help="Selecione os portes de empresa"
        )
        if tamanhos_selecionados:
            for tamanho in tamanhos_selecionados:
                st.markdown(f'<span class="filter-pill">🏢 {tamanho}</span>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- FILTRO ADICIONAL: FAIXA SALARIAL ---
    st.markdown("""
        <div class="filter-section">
            <div class="filter-header">
                <span class="filter-icon">💰</span>
                <span>Faixa Salarial (USD)</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    usar_filtro_salario = st.checkbox("Ativar filtro de salário", value=False)
    
    if usar_filtro_salario:
        salario_min = int(df['usd'].min())
        salario_max = int(df['usd'].max())
        
        faixa_salario = st.slider(
            "Selecione a faixa:",
            min_value=salario_min,
            max_value=salario_max,
            value=(salario_min, salario_max),
            step=10000,
            format="$%d"
        )
        st.info(f"💵 De ${faixa_salario[0]:,} até ${faixa_salario[1]:,}")
    else:
        faixa_salario = (int(df['usd'].min()), int(df['usd'].max()))
    
    st.markdown("---")
    
    # --- AÇÕES RÁPIDAS ---
    st.markdown("### ⚡ Ações Rápidas")
    
    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        if st.button("🔄 Resetar", use_container_width=True, type="secondary"):
            st.rerun()
    
    with col_btn2:
        if st.button("📊 Aplicar", use_container_width=True, type="primary"):
            st.success("✅ Filtros aplicados!")
    
    st.markdown("---")
    
    # --- RESUMO DOS FILTROS ---
    with st.expander("📋 Resumo dos Filtros Ativos", expanded=False):
        st.markdown(f"""
        - **Anos:** {len(anos_selecionados)} selecionado(s)
        - **Senioridades:** {len(senioridades_selecionadas)} selecionada(s)
        - **Contratos:** {len(contratos_selecionados)} selecionado(s)
        - **Tamanhos:** {len(tamanhos_selecionados)} selecionado(s)
        - **Faixa Salarial:** {"Ativa" if usar_filtro_salario else "Desativada"}
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dica final
    st.markdown("""
        <div style="background-color: #ffffff; padding: 1rem; border-radius: 8px; border-left: 4px solid #1f77b4; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <strong>💡 Dica:</strong><br>
            Use os filtros para explorar diferentes segmentos do mercado de dados e descobrir insights valiosos!
        </div>
    """, unsafe_allow_html=True)

# --- Filtragem do DataFrame ---
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados)) &
    (df['usd'] >= faixa_salario[0]) &
    (df['usd'] <= faixa_salario[1])
]

# --- Conteúdo Principal ---
# Header com ícone e descrição
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.title("💼 Dashboard de Análise de Salários na Área de Dados")
    st.markdown("""
    <div class="tooltip-info">
        📈 Explore tendências salariais, compare cargos e descubra insights sobre o mercado de dados.
        Utilize os <strong>filtros à esquerda</strong> para refinar sua análise.
    </div>
    """, unsafe_allow_html=True)

with col_header2:
    percentual_filtrado = (len(df_filtrado) / len(df) * 100) if len(df) > 0 else 0
    st.metric(
        label="Dados Filtrados",
        value=f"{len(df_filtrado):,}",
        delta=f"{percentual_filtrado:.1f}% do total"
    )

# Verificação de dados
if df_filtrado.empty:
    st.error("⚠️ Nenhum dado corresponde aos filtros selecionados. Por favor, ajuste os filtros na barra lateral.")
    st.stop()

st.markdown("---")

# --- Métricas Principais (KPIs) ---
st.subheader("📊 Principais Indicadores")

# Cálculo das métricas
salario_medio = df_filtrado['usd'].mean()
salario_mediano = df_filtrado['usd'].median()
salario_maximo = df_filtrado['usd'].max()
salario_minimo = df_filtrado['usd'].min()
total_registros = df_filtrado.shape[0]
cargo_mais_frequente = df_filtrado["cargo"].mode()[0] if not df_filtrado.empty else "N/A"

# Exibir métricas em colunas
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="💰 Salário Médio",
        value=f"${salario_medio:,.0f}",
        help="Média salarial anual em USD"
    )

with col2:
    st.metric(
        label="📊 Salário Mediano",
        value=f"${salario_mediano:,.0f}",
        help="Valor mediano dos salários"
    )

with col3:
    st.metric(
        label="🎯 Salário Máximo",
        value=f"${salario_maximo:,.0f}",
        help="Maior salário registrado"
    )

with col4:
    st.metric(
        label="📉 Salário Mínimo",
        value=f"${salario_minimo:,.0f}",
        help="Menor salário registrado"
    )

with col5:
    st.metric(
        label="👨‍💼 Cargo Comum",
        value=cargo_mais_frequente[:20] + "..." if len(cargo_mais_frequente) > 20 else cargo_mais_frequente,
        help="Cargo mais frequente nos dados"
    )

st.markdown("---")

# --- Análises Visuais com Plotly ---
st.subheader("📈 Visualizações Interativas")

# Abas para organizar melhor os gráficos
tab1, tab2, tab3 = st.tabs(["💼 Cargos e Salários", "🌍 Análise Geográfica", "📊 Distribuições"])

with tab1:
    col_graf1, col_graf2 = st.columns(2)
    
    with col_graf1:
        st.markdown("#### Top 10 Cargos por Salário Médio")
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            labels={'usd': 'Salário Médio Anual (USD)', 'cargo': 'Cargo'},
            color='usd',
            color_continuous_scale='Blues'
        )
        grafico_cargos.update_layout(
            showlegend=False,
            yaxis={'categoryorder':'total ascending'},
            height=400,
            hovermode='closest'
        )
        grafico_cargos.update_traces(
            hovertemplate='<b>%{y}</b><br>Salário: $%{x:,.0f}<extra></extra>'
        )
        st.plotly_chart(grafico_cargos, use_container_width=True)
    
    with col_graf2:
        st.markdown("#### Salário Médio por Senioridade")
        salario_senioridade = df_filtrado.groupby('senioridade')['usd'].mean().reset_index()
        
        grafico_senioridade = px.bar(
            salario_senioridade,
            x='senioridade',
            y='usd',
            labels={'usd': 'Salário Médio (USD)', 'senioridade': 'Nível'},
            color='usd',
            color_continuous_scale='Greens'
        )
        grafico_senioridade.update_layout(
            showlegend=False,
            height=400
        )
        grafico_senioridade.update_traces(
            hovertemplate='<b>%{x}</b><br>Salário: $%{y:,.0f}<extra></extra>'
        )
        st.plotly_chart(grafico_senioridade, use_container_width=True)
    
    # Gráfico de linha: Evolução salarial ao longo dos anos
    st.markdown("#### Evolução Salarial por Ano")
    evolucao_ano = df_filtrado.groupby('ano')['usd'].mean().reset_index()
    
    grafico_evolucao = px.line(
        evolucao_ano,
        x='ano',
        y='usd',
        markers=True,
        labels={'usd': 'Salário Médio (USD)', 'ano': 'Ano'}
    )
    grafico_evolucao.update_traces(
        line_color='#1f77b4',
        line_width=3,
        marker=dict(size=10),
        hovertemplate='<b>Ano %{x}</b><br>Salário: $%{y:,.0f}<extra></extra>'
    )
    grafico_evolucao.update_layout(height=350)
    st.plotly_chart(grafico_evolucao, use_container_width=True)

with tab2:
    col_geo1, col_geo2 = st.columns(2)
    
    with col_geo1:
        st.markdown("#### Mapa: Salário Médio de Data Scientist por País")
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
            
            grafico_paises = px.choropleth(
                media_ds_pais,
                locations='residencia_iso3',
                color='usd',
                color_continuous_scale='RdYlGn',
                labels={'usd': 'Salário Médio (USD)', 'residencia_iso3': 'País'},
                hover_data={'usd': ':,.0f'}
            )
            grafico_paises.update_layout(
                height=500,
                geo=dict(showframe=False, showcoastlines=True)
            )
            st.plotly_chart(grafico_paises, use_container_width=True)
        else:
            st.warning("⚠️ Nenhum dado de Data Scientist disponível com os filtros atuais.")
    
    with col_geo2:
        st.markdown("#### Top 10 Países por Salário Médio")
        top_paises = df_filtrado.groupby('residencia_iso3')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        
        grafico_top_paises = px.bar(
            top_paises,
            x='usd',
            y='residencia_iso3',
            orientation='h',
            labels={'usd': 'Salário Médio (USD)', 'residencia_iso3': 'País'},
            color='usd',
            color_continuous_scale='Viridis'
        )
        grafico_top_paises.update_layout(
            showlegend=False,
            height=500
        )
        grafico_top_paises.update_traces(
            hovertemplate='<b>%{y}</b><br>Salário: $%{x:,.0f}<extra></extra>'
        )
        st.plotly_chart(grafico_top_paises, use_container_width=True)

with tab3:
    col_dist1, col_dist2 = st.columns(2)
    
    with col_dist1:
        st.markdown("#### Distribuição de Salários")
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            labels={'usd': 'Salário Anual (USD)', 'count': 'Frequência'},
            color_discrete_sequence=['#1f77b4']
        )
        grafico_hist.update_layout(
            showlegend=False,
            height=400
        )
        grafico_hist.update_traces(
            hovertemplate='Faixa: $%{x:,.0f}<br>Quantidade: %{y}<extra></extra>'
        )
        st.plotly_chart(grafico_hist, use_container_width=True)
    
    with col_dist2:
        st.markdown("#### Proporção dos Tipos de Trabalho")
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        grafico_remoto.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Quantidade: %{value}<br>Percentual: %{percent}<extra></extra>'
        )
        grafico_remoto.update_layout(height=400)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    
    # Gráfico adicional: Tamanho da empresa
    st.markdown("#### Distribuição por Tamanho de Empresa")
    tamanho_empresa = df_filtrado['tamanho_empresa'].value_counts().reset_index()
    tamanho_empresa.columns = ['tamanho', 'quantidade']
    
    grafico_tamanho = px.bar(
        tamanho_empresa,
        x='tamanho',
        y='quantidade',
        labels={'tamanho': 'Tamanho da Empresa', 'quantidade': 'Número de Registros'},
        color='quantidade',
        color_continuous_scale='Blues'
    )
    grafico_tamanho.update_layout(showlegend=False, height=350)
    st.plotly_chart(grafico_tamanho, use_container_width=True)

st.markdown("---")

# --- Tabela de Dados Detalhados ---
st.subheader("📋 Dados Detalhados")

# Opção para mostrar/ocultar a tabela
mostrar_tabela = st.checkbox("Mostrar tabela de dados completa", value=False)

if mostrar_tabela:
    # Opções de visualização
    col_opcoes1, col_opcoes2 = st.columns(2)
    
    with col_opcoes1:
        num_linhas = st.selectbox(
            "Número de linhas para exibir:",
            [10, 25, 50, 100, "Todos"],
            index=0
        )
    
    with col_opcoes2:
        colunas_exibir = st.multiselect(
            "Selecione as colunas:",
            df_filtrado.columns.tolist(),
            default=df_filtrado.columns.tolist()
        )
    
    # Exibir tabela
    if num_linhas == "Todos":
        st.dataframe(
            df_filtrado[colunas_exibir],
            use_container_width=True,
            height=400
        )
    else:
        st.dataframe(
            df_filtrado[colunas_exibir].head(num_linhas),
            use_container_width=True,
            height=400
        )
    
    # Botão de download
    csv = df_filtrado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download dos dados filtrados (CSV)",
        data=csv,
        file_name='dados_salarios_filtrados.csv',
        mime='text/csv',
        use_container_width=True
    )
else:
    st.info("👆 Marque a caixa acima para visualizar a tabela de dados completa")

# --- Footer ---
st.markdown("---")
col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.caption("📊 Dashboard criado com Streamlit")

with col_footer2:
    st.caption("💾 Dados atualizados regularmente")

with col_footer3:
    st.caption("🔍 Use os filtros para análises personalizadas")
