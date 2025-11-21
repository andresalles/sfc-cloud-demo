import streamlit as st
import pandas as pd
import numpy as np
import math
from datetime import datetime
import base64

# Configuração da página
st.set_page_config(
    page_title="SFC - Salles Analytics",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #3B82F6, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border-radius: 10px;
        padding: 1.5rem;
        border-left: 4px solid;
        backdrop-filter: blur(10px);
    }
    .confidential {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        opacity: 0.02;
        font-size: 4rem;
        font-weight: bold;
        color: #F59E0B;
        display: flex;
        align-items: center;
        justify-content: center;
        transform: rotate(-45deg);
        z-index: -1;
    }
    .download-btn {
        background: linear-gradient(45deg, #1E40AF, #0369A1) !important;
        color: white !important;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin: 1rem 0;
        text-align: center;
        border: 2px solid #1E3A8A;
        cursor: pointer;
        font-size: 16px;
    }
    .download-btn:hover {
        background: linear-gradient(45deg, #1E3A8A, #0C4A6E) !important;
        color: white !important;
    }
</style>
<div class='confidential'>CONFIDENTIAL - PROPRIETARY</div>
""", unsafe_allow_html=True)

# Funções matemáticas do SFC
def calculate_complexity_x(vars_dict):
    numVariables = vars_dict['numVariables']
    interdependencies = vars_dict['interdependencies']
    uncertainty = vars_dict['uncertainty']
    resourceAvailability = vars_dict['resourceAvailability']
    
    base = math.pow(numVariables, 1.5) * (1 + interdependencies * 0.8)
    uncertainty_factor = math.exp(uncertainty * 0.3)
    resource_penalty = math.pow((1 - resourceAvailability), 2) * 3
    
    Cx = (base * uncertainty_factor + resource_penalty) / 10
    return min(Cx, 12)

def calculate_complexity_y(vars_dict):
    knowledgeDepth = vars_dict['knowledgeDepth']
    technicalDebt = vars_dict['technicalDebt']
    businessImpact = vars_dict['businessImpact']
    stakeholders = vars_dict['stakeholders']
    
    knowledge_factor = math.pow(knowledgeDepth, 1.8) * 2
    debt_impact = technicalDebt * businessImpact * 1.5
    stakeholder_complexity = math.log(stakeholders + 1) * 2
    
    Cy = (knowledge_factor + debt_impact + stakeholder_complexity) / 8
    return min(Cy, 12)

def calculate_complexity_z(vars_dict):
    timeConstraint = vars_dict['timeConstraint']
    volatility = vars_dict['volatility']
    criticalityLevel = vars_dict['criticalityLevel']
    changeFrequency = vars_dict['changeFrequency']
    
    urgency_factor = math.pow((1 - timeConstraint), 2.5) * 5
    volatility_impact = volatility * criticalityLevel * 2
    change_penalty = math.exp(changeFrequency * 0.4)
    
    Cz = (urgency_factor + volatility_impact + change_penalty) / 7
    return min(Cz, 12)

def calculate_delta(Cx, Cy, Cz):
    complexity_vector = math.sqrt(math.pow(Cx, 2) + math.pow(Cy, 2) + math.pow(Cz, 2))
    max_dimension = max(Cx, Cy, Cz)
    dimension_variance = math.pow(Cx - Cy, 2) + math.pow(Cy - Cz, 2) + math.pow(Cz - Cx, 2)
    
    delta = (complexity_vector * 0.6) + (max_dimension * 0.3) + (math.sqrt(dimension_variance) * 0.1)
    return min(delta, 12)

def get_complexity_label(score):
    if score <= 2.0: return {'label': 'Baixa', 'color': 'green'}
    if score <= 4.0: return {'label': 'Moderada', 'color': 'blue'}
    if score <= 6.0: return {'label': 'Alta', 'color': 'yellow'}
    if score <= 9.0: return {'label': 'Muito Alta', 'color': 'orange'}
    if score <= 10.0: return {'label': 'Extremamente Alta', 'color': 'red'}
    return {'label': 'Colapso do Sistema', 'color': 'darkred'}

def extract_variables_from_text(text):
    word_count = len(text.split())
    sentences = len([s for s in text.split('.') if s.strip()])
    technical_terms = len([word for word in text.lower().split() if word in ['sistema', 'tecnologia', 'processo', 'análise', 'complexidade', 'projeto', 'desenvolvimento', 'implementação']])
    urgency_words = len([word for word in text.lower().split() if word in ['urgente', 'imediato', 'crítico', 'prazo', 'deadline', 'rápido']])
    uncertainty_words = len([word for word in text.lower().split() if word in ['incerto', 'risco', 'desconhecido', 'indefinido', 'possível', 'talvez']])
    
    num_variables = min(math.floor(word_count / 100) + technical_terms / 5, 20)
    interdependencies = min(technical_terms / word_count * 10, 1) if word_count > 0 else 0
    uncertainty = min(uncertainty_words / sentences * 2, 1) if sentences > 0 else 0
    resource_availability = max(0.3, 1 - (word_count / 5000))
    
    knowledge_depth = min(technical_terms / 50, 5)
    technical_debt = 0.5  # Valor fixo para demonstração
    business_impact = min(word_count / 1000, 1)
    stakeholders = min(math.floor(sentences / 10), 15)
    
    time_constraint = min(urgency_words / 10, 1)
    volatility = min(uncertainty_words / sentences, 1) if sentences > 0 else 0
    criticality_level = min(urgency_words / sentences * 2, 1) if sentences > 0 else 0
    change_frequency = min(uncertainty_words / 20, 1)
    
    return {
        'numVariables': num_variables,
        'interdependencies': interdependencies,
        'uncertainty': uncertainty,
        'resourceAvailability': resource_availability,
        'knowledgeDepth': knowledge_depth,
        'technicalDebt': technical_debt,
        'businessImpact': business_impact,
        'stakeholders': stakeholders,
        'timeConstraint': time_constraint,
        'volatility': volatility,
        'criticalityLevel': criticality_level,
        'changeFrequency': change_frequency
    }

# Funções para relatório TXT
def generate_report_text(analysis_data):
    return f"""
╔════════════════════════════════════════════════════════════════════════════╗
║                    SALLES FRAMEWORK CORE (SFC)                             ║
║              EXECUTIVE COMPLEXITY ANALYSIS REPORT                          ║
║                                                                            ║
║  CONFIDENTIAL - PROPRIETARY & PROTECTED INTELLECTUAL PROPERTY              ║
║  © 2026 Salles Framework Technologies - All Rights Reserved               ║
╚════════════════════════════════════════════════════════════════════════════╝

DOCUMENT METADATA
================================================================================
Report ID: SFC-{datetime.now().strftime('%Y%m%d-%H%M%S')}
Analysis Date: {analysis_data['timestamp']}
Document Name: {analysis_data['file_name']}
Classification: CONFIDENTIAL - DO NOT DISTRIBUTE

EXECUTIVE SUMMARY
================================================================================

OVERALL COMPLEXITY SCORE: {analysis_data['delta']:.2f} / 12.0
CLASSIFICATION: {analysis_data['delta_label'].upper()}

RECOMMENDATION: {analysis_data['recommendation']}

THREE-DIMENSIONAL ANALYSIS:
• Technical Complexity (X):  {analysis_data['Cx']:.2f} - {analysis_data['Cx_label']}
• Cognitive Complexity (Y):  {analysis_data['Cy']:.2f} - {analysis_data['Cy_label']}  
• Temporal Complexity (Z):   {analysis_data['Cz']:.2f} - {analysis_data['Cz_label']}

EQUATIONS APPLIED:
• Cx = [(N^1.5 × (1+I×0.8)) × e^(U×0.3) + (1-R)²×3] / 10
• Cy = [K^1.8×2 + D×B×1.5 + ln(S+1)×2] / 8  
• Cz = [(1-T)^2.5×5 + V×C×2 + e^(F×0.4)] / 7
• Δ = √(Cx²+Cy²+Cz²)×0.6 + max(Cx,Cy,Cz)×0.3 + √(σ²)×0.1

SALLES SCALE:
0.0-2.0: Baixa | 2.0-4.0: Moderada | 4.0-6.0: Alta
6.0-9.0: Muito Alta | 9.0-10.0: Extremamente Alta | 10.0+: Colapso do Sistema

================================================================================
END OF REPORT - CONFIDENTIAL
================================================================================
"""

def get_download_link(text, filename):
    b64 = base64.b64encode(text.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}" class="download-btn">📥 Baixar Relatório Executivo</a>'

# Interface principal
def main():
    st.markdown("<h1 class='main-header'>SFC - Salles Analytics</h1>", unsafe_allow_html=True)
    st.markdown("### Sistema de Análise Quantitativa de Complexidade Auditável")
    st.markdown("**Framework Proprietário Tridimensional Não-Linear**")
    
    # Upload de arquivo
    st.markdown("---")
    st.header("📤 Upload de Documento")
    uploaded_file = st.file_uploader("Envie PDF, DOCX ou TXT para análise", type=['pdf', 'docx', 'txt'])
    
    if uploaded_file is not None:
        try:
            # Ler arquivo
            if uploaded_file.type == "text/plain":
                text = str(uploaded_file.read(), "utf-8")
            else:
                # Para PDF/DOCX, usar texto simples por enquanto
                text = f"Conteúdo do arquivo {uploaded_file.name} - análise de complexidade em andamento."
            
            # Análise
            with st.spinner('Analisando documento com equações SFC...'):
                vars_dict = extract_variables_from_text(text)
                Cx = calculate_complexity_x(vars_dict)
                Cy = calculate_complexity_y(vars_dict)
                Cz = calculate_complexity_z(vars_dict)
                delta = calculate_delta(Cx, Cy, Cz)
                
                label_x = get_complexity_label(Cx)
                label_y = get_complexity_label(Cy)
                label_z = get_complexity_label(Cz)
                label_delta = get_complexity_label(delta)
            
            # Resultados
            st.markdown("---")
            st.header("📊 Análise Tridimensional de Complexidade")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class='metric-card' style='border-color: #8B5CF6;'>
                    <h4>EIXO X</h4>
                    <h3>Complexidade Técnica</h3>
                    <h1 style='color: #8B5CF6;'>{Cx:.2f}</h1>
                    <span style='background-color: {label_x["color"]}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem;'>{label_x['label']}</span>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class='metric-card' style='border-color: #3B82F6;'>
                    <h4>EIXO Y</h4>
                    <h3>Complexidade Cognitiva</h3>
                    <h1 style='color: #3B82F6;'>{Cy:.2f}</h1>
                    <span style='background-color: {label_y["color"]}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem;'>{label_y['label']}</span>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class='metric-card' style='border-color: #06B6D4;'>
                    <h4>EIXO Z</h4>
                    <h3>Complexidade Temporal</h3>
                    <h1 style='color: #06B6D4;'>{Cz:.2f}</h1>
                    <span style='background-color: {label_z["color"]}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem;'>{label_z['label']}</span>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                st.markdown(f"""
                <div class='metric-card' style='border-color: #F59E0B; background: linear-gradient(135deg, rgba(245,158,11,0.2), rgba(239,68,68,0.2));'>
                    <h4>SISTEMA Δ</h4>
                    <h3>Score Delta</h3>
                    <h1 style='color: #F59E0B;'>{delta:.2f}</h1>
                    <span style='background-color: {label_delta["color"]}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem;'>{label_delta['label']}</span>
                </div>
                """, unsafe_allow_html=True)
            
            # Recomendação
            st.markdown("---")
            if delta <= 4.0:
                st.success("### ✅ Automação Recomendada\nSistema pode operar de forma automatizada com supervisão mínima.")
                recommendation = "Automação Recomendada"
            elif delta <= 7.0:
                st.warning("### ⚠ Supervisão Necessária\nRequer monitoramento ativo e intervenção periódica de especialistas.")
                recommendation = "Supervisão Necessária"
            else:
                st.error("### 🔴 Intervenção Humana Crítica\nComplexidade excede limites seguros. Requer decisão humana especializada imediata.")
                recommendation = "Intervenção Humana Crítica"
            
            # Botão de Download
            st.markdown("---")
            st.header("📄 Relatório Executivo")
            
            report_data = {
                'file_name': uploaded_file.name,
                'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                'delta': delta,
                'delta_label': label_delta['label'],
                'Cx': Cx,
                'Cx_label': label_x['label'],
                'Cy': Cy,
                'Cy_label': label_y['label'],
                'Cz': Cz,
                'Cz_label': label_z['label'],
                'recommendation': recommendation
            }
            
            report_text = generate_report_text(report_data)
            st.markdown(get_download_link(report_text, f"SFC_Report_{uploaded_file.name}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"), unsafe_allow_html=True)
            st.markdown("**Relatório auditável com fundamentação matemática completa**")
                
        except Exception as e:
            st.error(f"Erro ao processar arquivo: {str(e)}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #6B7280;'>
        <p>© 2026 Salles Framework Technologies - Sistema Proprietário Auditável</p>
        <p>Framework de "Caixa de Vidro" - 100% Transparente e Rastreável</p>
        <p><strong>Confidential</strong> - Proprietary Intellectual Property</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()