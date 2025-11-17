#!/usr/bin/env python3
"""
SALLES FRAMEWORK CORE (SFC) - CLOUD EDITION
Versão otimizada para deploy em nuvem
Autor: André Salles
Data: Novembro 2025 - Preparação TECPAR 2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
import hashlib
import math
import sys
import os

# ==================================================
# SISTEMA DE LOGIN - PROTÓTIPO TECPAR
# ==================================================

class LoginSFC:
    """Sistema de autenticação simples para demonstração"""
    
    @staticmethod
    def gerar_hash(senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()
    
    @staticmethod
    def verificar_login(usuario: str, senha: str) -> bool:
        SENHA_HASH = "15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225"
        return (usuario == "admin" and 
                LoginSFC.gerar_hash(senha) == SENHA_HASH)
    
    @staticmethod
    def tela_login():
        st.markdown("""
        <style>
            .login-header {
                text-align: center;
                color: #1f77b4;
                margin-bottom: 2rem;
            }
            .login-container {
                max-width: 400px;
                margin: 0 auto;
                padding: 2rem;
                border: 1px solid #ddd;
                border-radius: 10px;
                background: #f9f9f9;
            }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="login-header"><h1>🧠 SFC - Acesso Restrito</h1></div>', 
                   unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="login-container">', unsafe_allow_html=True)
            
            usuario = st.text_input("👤 Usuário", placeholder="Digite o usuário")
            senha = st.text_input("🔒 Senha", type="password", placeholder="Digite a senha")
            
            if st.button("🚀 Acessar Sistema", type="primary", use_container_width=True):
                if LoginSFC.verificar_login(usuario, senha):
                    st.session_state.logado = True
                    st.session_state.usuario = usuario
                    st.success("✅ Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("❌ Usuário ou senha incorretos!")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            with st.expander("ℹ️ Credenciais para Demonstração"):
                st.write("**Para acesso durante a apresentação:**")
                st.code("Usuário: admin\nSenha: 123456789")

# ==================================================
# EQUAÇÕES MATEMÁTICAS SFC (CÓDIGO REUTILIZADO)
# ==================================================

class EquacoesSFC:
    """Equações proprietárias do SFC - Versão Cloud"""
    
    ALPHA_1 = 0.05
    ALPHA_2 = 8.0
    ALPHA_3 = 6.0
    BETA_1 = 5.0
    BETA_2 = 7.0
    GAMA_1 = 8.0
    GAMA_2 = 6.0
    
    @staticmethod
    def calcular_complexidade_tecnica(num_variaveis_tecnicas, interdependencias, fator_incerteza, disponibilidade_recursos):
        termo1 = EquacoesSFC.ALPHA_1 * num_variaveis_tecnicas
        termo2 = EquacoesSFC.ALPHA_2 * interdependencias * (1 + fator_incerteza)
        termo3 = EquacoesSFC.ALPHA_3 * (1 - disponibilidade_recursos)
        cx = termo1 + termo2 + termo3
        return min(max(cx, 0.0), 12.0)
    
    @staticmethod
    def calcular_complexidade_cognitiva(profundidade_conhecimento, nivel_divida_tecnica, impacto_negocio):
        termo1 = EquacoesSFC.BETA_1 * profundidade_conhecimento * math.log(1 + 10 * nivel_divida_tecnica)
        termo2 = EquacoesSFC.BETA_2 * impacto_negocio
        cy = termo1 + termo2
        return min(max(cy, 0.0), 12.0)
    
    @staticmethod
    def calcular_complexidade_temporal(restricoes_temporais, tempo_disponivel, volatilidade):
        termo1 = EquacoesSFC.GAMA_1 * restricoes_temporais / (1 + tempo_disponivel / 30)
        termo2 = EquacoesSFC.GAMA_2 * volatilidade
        cz = termo1 + termo2
        return min(max(cz, 0.0), 12.0)
    
    @staticmethod
    def calcular_score_salles(cx, cy, cz, delta_instabilidade, dominio):
        from math import sqrt
        multiplicador_dominio = CalibracaoDominios.obter_multiplicador(dominio)
        norma_euclidiana = sqrt(cx**2 + cy**2 + cz**2)
        fator_amortecimento = 1 + delta_instabilidade**2
        score = multiplicador_dominio * norma_euclidiana / fator_amortecimento
        return min(max(score, 0.0), 12.0)

# ==================================================
# CALIBRAÇÃO POR DOMÍNIOS (CÓDIGO REUTILIZADO)
# ==================================================

class CalibracaoDominios:
    """Sistema de calibração por domínios - Versão Cloud"""
    
    DOMINIOS = {
        'gestao_projetos': 1.0, 'consultoria': 1.0, 'educacao': 1.0,
        'agricultura': 1.1, 'governo': 1.1, 'varejo': 1.1,
        'financeiro': 1.2, 'seguros': 1.2, 'manufatura': 1.2, 'logistica': 1.2,
        'tecnologia': 1.3, 'telecom': 1.3, 'infraestrutura': 1.3,
        'saude': 1.4, 'energia': 1.4, 'aeroespacial': 1.4
    }
    
    @staticmethod
    def obter_multiplicador(dominio):
        dominio_normalizado = dominio.lower().strip().replace(' ', '_')
        return CalibracaoDominios.DOMINIOS.get(dominio_normalizado, 1.0)
    
    @staticmethod
    def listar_dominios():
        return sorted(CalibracaoDominios.DOMINIOS.keys())

# ==================================================
# SISTEMA DELTA ADAPTATIVO (CÓDIGO REUTILIZADO)
# ==================================================

class SistemaDelta:
    """Sistema Delta Adaptativo - Versão Cloud"""
    
    def __init__(self, tamanho_historico=100):
        self.tamanho_historico = tamanho_historico
        self.historico = []
        self.threshold_alerta = 4.0
        self.threshold_critico = 8.0
        self.total_avaliacoes = 0
    
    def registrar(self, score, metadata=None):
        registro = {
            'score': float(score),
            'timestamp': datetime.now().isoformat(),
            'metadata': metadata or {}
        }
        self.historico.append(registro)
        if len(self.historico) > self.tamanho_historico:
            self.historico.pop(0)
        if len(self.historico) >= 10:
            self._recalibrar_thresholds()
        self.total_avaliacoes += 1
    
    def _recalibrar_thresholds(self):
        if len(self.historico) < 10:
            return
        scores = [registro['score'] for registro in self.historico]
        self.threshold_alerta = float(np.percentile(scores, 50))
        self.threshold_critico = float(np.percentile(scores, 80))
    
    def avaliar(self, score):
        if not (0.0 <= score <= 12.0):
            raise ValueError("Score deve estar entre 0.0 e 12.0")
        
        if score < 4.0:
            nivel = "MONITORAMENTO_NORMAL"
            urgencia = 0.0
        elif score < self.threshold_critico:
            if score < self.threshold_alerta:
                nivel = "MONITORAMENTO_NORMAL"
            else:
                nivel = "ALERTA_TATICO"
            urgencia = 0.3
        elif score < 10.0:
            nivel = "ESCALAMENTO_ESTRATEGICO"
            urgencia = 0.7
        else:
            nivel = "INTERVENCAO_HUMANA_OBRIGATORIA"
            urgencia = 1.0
        
        self.registrar(score)
        
        return {
            'nivel': nivel,
            'urgencia': urgencia,
            'score': score,
            'threshold_alerta': self.threshold_alerta,
            'threshold_critico': self.threshold_critico,
            'timestamp': datetime.now().isoformat()
        }

# ==================================================
# APLICAÇÃO PRINCIPAL SFC CLOUD
# ==================================================

class SFCAppCloud:
    """Aplicação principal do SFC Cloud Edition"""
    
    def __init__(self):
        self.sistema_delta = SistemaDelta()
        self.carregar_historico()
    
    def carregar_historico(self):
        """Carrega histórico da sessão atual"""
        if 'historico_sfc' not in st.session_state:
            st.session_state.historico_sfc = []
    
    def salvar_analise(self, dados):
        """Salva análise no histórico da sessão"""
        st.session_state.historico_sfc.append(dados)
    
    def determinar_faixa_complexidade(self, score):
        """Determina faixa baseada na Escala de Salles (0-12)"""
        if score < 2.0: return "Muito Baixa", "muito-baixa", "🟢"
        elif score < 4.0: return "Baixa", "baixa", "🟢"
        elif score < 6.0: return "Moderada", "moderada", "🟡"
        elif score < 8.0: return "Alta", "alta", "🟠"
        elif score < 10.0: return "Muito Alta", "muito-alta", "🔴"
        elif score < 11.0: return "Extrema", "extrema", "🟣"
        else: return "Catastrófica", "catastrofica", "⚫"
    
    def criar_visualizacao_radar(self, cx, cy, cz):
        """Cria gráfico radar das complexidades"""
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=[cx, cy, cz],
            theta=['Técnica', 'Cognitiva', 'Temporal'],
            fill='toself',
            name='Perfil de Complexidade',
            line=dict(color='#1f77b4')
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 12])),
            showlegend=False,
            title="Perfil 3D de Complexidade",
            height=400
        )
        return fig

# ==================================================
# CONFIGURAÇÃO E EXECUÇÃO
# ==================================================

def main():
    # Configuração da página
    st.set_page_config(
        page_title="SFC Cloud Edition",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Sistema de Login
    if not hasattr(st.session_state, 'logado'):
        st.session_state.logado = False
    
    if not st.session_state.logado:
        LoginSFC.tela_login()
        return
    
    # Aplicação principal (após login)
    app = SFCAppCloud()
    
    # Header após login
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown('<div class="main-header">🧠 Salles Framework Core - Cloud Edition</div>', 
                   unsafe_allow_html=True)
    with col3:
        if st.button("🚪 Sair"):
            st.session_state.logado = False
            st.rerun()
    
    # CSS personalizado
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .score-card {
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
    .muito-baixa { background: linear-gradient(135deg, #00b894 0%, #00a085 100%); }
    .baixa { background: linear-gradient(135deg, #00cec9 0%, #00b5b0 100%); }
    .moderada { background: linear-gradient(135deg, #fdcb6e 0%, #fdbb4a 100%); }
    .alta { background: linear-gradient(135deg, #e17055 0%, #d65f44 100%); }
    .muito-alta { background: linear-gradient(135deg, #d63031 0%, #c23616 100%); }
    .extrema { background: linear-gradient(135deg, #6c5ce7 0%, #5d4fe0 100%); }
    .catastrofica { background: linear-gradient(135deg, #2d3436 0%, #1e2224 100%); }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar - Controles
    with st.sidebar:
        st.header("⚙️ Configurações")
        usuario = st.text_input("👤 Seu Nome", value="Analista TECPAR")
        dominio = st.selectbox("🏢 Domínio", options=CalibracaoDominios.listar_dominios())
        
        st.markdown("---")
        st.header("📊 Parâmetros de Entrada")
        
        tab1, tab2, tab3 = st.tabs(["Técnica", "Cognitiva", "Temporal"])
        
        with tab1:
            num_variaveis_tecnicas = st.slider("Nº Variáveis Técnicas", 1, 100, 25)
            interdependencias = st.slider("Interdependências", 0.0, 1.0, 0.5, 0.1)
            fator_incerteza = st.slider("Fator Incerteza", 0.0, 1.0, 0.3, 0.1)
            disponibilidade_recursos = st.slider("Disponibilidade Recursos", 0.0, 1.0, 0.7, 0.1)
        
        with tab2:
            profundidade_conhecimento = st.slider("Profundidade Conhecimento", 0.0, 1.0, 0.5, 0.1)
            nivel_divida_tecnica = st.slider("Dívida Técnica", 0.0, 1.0, 0.3, 0.1)
            impacto_negocio = st.slider("Impacto Negócio", 0.0, 1.0, 0.6, 0.1)
        
        with tab3:
            restricoes_temporais = st.slider("Restrições Temporais", 0.0, 1.0, 0.4, 0.1)
            tempo_disponivel = st.slider("Tempo Disponível (dias)", 1, 365, 30)
            volatilidade = st.slider("Volatilidade", 0.0, 1.0, 0.3, 0.1)
            delta_instabilidade = st.slider("Δ Instabilidade", 0.0, 1.0, 0.2, 0.1)
    
    # Área principal
    tab_analise, tab_historico, tab_info = st.tabs(["📈 Análise", "📊 Histórico", "ℹ️ Informações"])
    
    with tab_analise:
        st.header("Análise de Complexidade")
        
        if st.button("🎯 Calcular Complexidade", type="primary"):
            with st.spinner("Calculando métricas de complexidade..."):
                parametros = {
                    'num_variaveis_tecnicas': num_variaveis_tecnicas,
                    'interdependencias': interdependencias,
                    'fator_incerteza': fator_incerteza,
                    'disponibilidade_recursos': disponibilidade_recursos,
                    'profundidade_conhecimento': profundidade_conhecimento,
                    'nivel_divida_tecnica': nivel_divida_tecnica,
                    'impacto_negocio': impacto_negocio,
                    'restricoes_temporais': restricoes_temporais,
                    'tempo_disponivel': tempo_disponivel,
                    'volatilidade': volatilidade,
                    'delta_instabilidade': delta_instabilidade,
                    'dominio': dominio
                }
                
                # Calcular complexidades
                cx = EquacoesSFC.calcular_complexidade_tecnica(
                    parametros['num_variaveis_tecnicas'],
                    parametros['interdependencias'],
                    parametros['fator_incerteza'],
                    parametros['disponibilidade_recursos']
                )
                cy = EquacoesSFC.calcular_complexidade_cognitiva(
                    parametros['profundidade_conhecimento'],
                    parametros['nivel_divida_tecnica'],
                    parametros['impacto_negocio']
                )
                cz = EquacoesSFC.calcular_complexidade_temporal(
                    parametros['restricoes_temporais'],
                    parametros['tempo_disponivel'],
                    parametros['volatilidade']
                )
                score = EquacoesSFC.calcular_score_salles(
                    cx, cy, cz,
                    parametros['delta_instabilidade'],
                    parametros['dominio']
                )
                
                # Avaliar com Sistema Delta
                avaliacao = app.sistema_delta.avaliar(score)
                faixa, classe_css, icone = app.determinar_faixa_complexidade(score)
                
                # Salvar na sessão
                registro = {
                    'usuario': usuario,
                    'dominio': dominio,
                    'parametros': parametros,
                    'resultados': {'cx': cx, 'cy': cy, 'cz': cz, 'score_salles': score},
                    'avaliacao_delta': avaliacao,
                    'timestamp': datetime.now().isoformat()
                }
                app.salvar_analise(registro)
                
                # Exibir resultados
                col1, col2, col3 = st.columns(3)
                with col1: st.metric("Complexidade Técnica", f"{cx:.2f}")
                with col2: st.metric("Complexidade Cognitiva", f"{cy:.2f}")
                with col3: st.metric("Complexidade Temporal", f"{cz:.2f}")
                
                # Score principal
                st.markdown(f"""
                <div class="score-card {classe_css}">
                    <h2>{icone} Score Salles: {score:.2f}/12.00</h2>
                    <h3>Faixa: {faixa}</h3>
                    <p>Ação Recomendada: {avaliacao['nivel']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Visualizações
                col_v1, col_v2 = st.columns(2)
                with col_v1:
                    fig_radar = app.criar_visualizacao_radar(cx, cy, cz)
                    st.plotly_chart(fig_radar, use_container_width=True)
    
    with tab_historico:
        st.header("Histórico da Sessão")
        if st.session_state.historico_sfc:
            dados_historico = []
            for registro in st.session_state.historico_sfc:
                dados_historico.append({
                    'Data': registro['timestamp'][:19],
                    'Usuário': registro['usuario'],
                    'Domínio': registro['dominio'],
                    'Score': registro['resultados']['score_salles'],
                    'Cx': registro['resultados']['cx'],
                    'Cy': registro['resultados']['cy'],
                    'Cz': registro['resultados']['cz']
                })
            df = pd.DataFrame(dados_historico)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("📝 Nenhuma análise realizada nesta sessão.")
    
    with tab_info:
        st.header("SFC Cloud Edition - Informações")
        st.markdown("""
        ### 🧠 Salles Framework Core - Cloud Edition
        
        **Versão:** Protótipo TECPAR 2025-2026
        **Desenvolvido por:** André Salles
        **Apresentação:** Marco Aurélio (Nov 2025) / TECPAR (Mar 2026)
        
        ### 📊 Escala de Complexidade de Salles (0.00 - 12.00)
        
        | Score | Faixa | Ação Recomendada |
        |-------|-------|------------------|
        | 0.00-2.00 | Muito Baixa | Monitoramento normal |
        | 2.00-4.00 | Baixa | Monitoramento normal |
        | 4.00-6.00 | Moderada | Alerta tático |
        | 6.00-8.00 | Alta | Escalamento estratégico |
        | 8.00-10.00 | Muito Alta | Escalamento estratégico |
        | 10.00-11.00 | Extrema | Intervenção humana obrigatória |
        | 11.00-12.00 | Catastrófica | Intervenção crítica imediata |
        """)

if __name__ == "__main__":
    main()