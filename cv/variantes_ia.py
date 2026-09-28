# -*- coding: utf-8 -*-
"""Remplacements qui transforment le CV banque en CV IA.

La source HTML (cv-fr.html / cv-en.html) porte la version banque. build-cv.py
applique ces couples (avant, apres) pour produire la variante IA, alignee sur le
portfolio https://sarrabendoub.github.io/ai : meme titre, meme presentation, et
les deux projets phares de cette page (CreditDoc-AI, News-Radar) a la place du
detail bancaire.
"""

ROLE_BANQUE = '<p class="role">Data Scientist &amp; AI Engineer · Financial Data · Risk · AI</p>'
ROLE_IA = '<p class="role">AI Engineer · Data Scientist · Generative AI · Document Intelligence · Machine Learning</p>'
URL_BANQUE = 'https://sarrabendoub.github.io/">sarrabendoub.github.io'
URL_IA = 'https://sarrabendoub.github.io/ai/">sarrabendoub.github.io/ai'

# ----------------------------------------------------------------- FRANCAIS
PROFIL_FR_AVANT = """    Ingénieure diplômée de l'École Nationale Supérieure d'Ingénieurs de Tunis (ENSIT) en
    mathématiques appliquées et modélisation,
    avec une expérience en Data Science et AI Engineering dans des environnements financiers et
    assurantiels. Je développe des solutions de Machine Learning, d'IA générative et de traitement
    intelligent des documents appliquées aux données financières, au risque et à l'analyse. Je recherche
    une opportunité en Data Science, AI Engineering ou Machine Learning."""

PROFIL_FR_APRES = """    Ingénieure diplômée de l'École Nationale Supérieure d'Ingénieurs de Tunis (ENSIT)
    en mathématiques appliquées et modélisation (2026), spécialisée en Data Science et IA, après une
    licence en Data Science à la Faculté des Sciences de Tunis (FST). Je construis des
    applications de Machine Learning et de LLM, des données brutes jusqu'à l'outil utilisé au
    quotidien : traitement intelligent des documents (IDP), RAG, agents IA et sorties structurées
    validées avant usage. Ouverte aux opportunités."""

PROJETS_FR_AVANT = """  <h2>Projets personnels — IA financière &amp; risque</h2>"""

PROJETS_FR_APRES = """  <h2>Projets personnels — IA &amp; Machine Learning</h2>"""

NEWSRADAR_FR_AVANT = """  <article class="item">
    <div class="row">
      <h3>CreditGuard — Scoring de crédit explicable et surveillé</h3>"""

NEWSRADAR_FR_APRES = """  <article class="item">
    <div class="row">
      <h3>News-Radar — Recherche sémantique &amp; chatbot RAG</h3>
      <span class="date">2026</span>
    </div>
    <p class="org">RAG · pgvector · Embeddings locaux · FastAPI</p>
    <ul>
      <li>Ingestion RSS planifiée et idempotente (~1 000 articles), embeddings calculés en local et stockés dans <strong>PostgreSQL / pgvector</strong> ; chatbot <strong>RAG</strong> ancré sur le corpus, API <strong>FastAPI</strong>.</li>
    </ul>
    <p class="tech"><b>Tech :</b> Python · FastAPI · PostgreSQL / pgvector · fastembed · Ollama · Docker</p>
  </article>

  <article class="item">
    <div class="row">
      <h3>CreditGuard — Scoring de crédit explicable et surveillé</h3>"""

# on compacte CreditGuard et FraudGuard pour tenir sur une page




# ----------------------------------------------------------------- ANGLAIS
PROFIL_EN_AVANT = """    Engineering graduate from the National School of Engineers of Tunis (ENSIT) in applied
    mathematics and modelling, with experience in Data
    Science and AI Engineering across financial and insurance environments. I build Machine Learning,
    Generative AI and intelligent document processing solutions for financial data, risk and analysis
    problems. I am looking for an opportunity in Data Science, AI Engineering or Machine Learning."""

PROFIL_EN_APRES = """    Engineering graduate from the National School of Engineers of Tunis (ENSIT) in applied
    mathematics and modelling (2026), specialised in Data Science and AI, with a BSc in Data Science
    from the Faculty of Sciences of Tunis (FST). I build Machine Learning and LLM
    applications, from raw data to the tool a team uses every day: intelligent document processing
    (IDP), retrieval-augmented generation (RAG), AI agents, and structured outputs that can be
    validated before anyone relies on them. Open to opportunities."""

PROJETS_EN_AVANT = """  <h2>Personal projects — Financial AI &amp; Risk</h2>"""

PROJETS_EN_APRES = """  <h2>Personal projects — AI &amp; Machine Learning</h2>"""

NEWSRADAR_EN_AVANT = """  <article class="item">
    <div class="row">
      <h3>CreditGuard — Explainable &amp; Monitored Credit Scoring</h3>"""

NEWSRADAR_EN_APRES = """  <article class="item">
    <div class="row">
      <h3>News-Radar — Semantic search &amp; RAG chatbot</h3>
      <span class="date">2026</span>
    </div>
    <p class="org">RAG · pgvector · Local embeddings · FastAPI</p>
    <ul>
      <li>Scheduled, idempotent RSS ingestion (~1,000 articles), embeddings computed locally and stored in <strong>PostgreSQL / pgvector</strong>; <strong>RAG</strong> chatbot grounded on the corpus, <strong>FastAPI</strong> backend.</li>
    </ul>
    <p class="tech"><b>Tech:</b> Python · FastAPI · PostgreSQL / pgvector · fastembed · Ollama · Docker</p>
  </article>

  <article class="item">
    <div class="row">
      <h3>CreditGuard — Explainable &amp; Monitored Credit Scoring</h3>"""






# --- compactage supplementaire pour tenir sur une page (variante IA) --------



DATAVIZ_FR_AVANT = """    <dt>Restitution &amp; Data Viz</dt><dd>Power BI · Matplotlib · Seaborn · Dashboards Streamlit</dd>
"""
DATAVIZ_FR_APRES = ""




DATAVIZ_EN_AVANT = """    <dt>Reporting &amp; Data Viz</dt><dd>Power BI · Matplotlib · Seaborn · Streamlit dashboards</dd>
"""
DATAVIZ_EN_APRES = ""


# La variante IA porte deux projets de plus : on resserre legerement l'interligne
# plutot que de sacrifier du contenu. La banque garde la mise en page d'origine.
DENSITE_AVANT = '<link rel="stylesheet" href="cv.css">'
DENSITE_APRES = (
    '<link rel="stylesheet" href="cv.css">\n'
    '<style>:root{--lh:1.16;--fs:7.85pt}.item{margin-bottom:2.6pt}.sec{margin-top:4pt}'
    '.pairs{row-gap:1.8pt}</style>'
)


# Sur le CV IA, la premiere ligne de competences ne parle plus de finance.
LIGNE1_FR_AVANT = "<dt>Données financières &amp; Risque</dt>"
LIGNE1_FR_APRES = "<dt>Data Science &amp; AI Engineering</dt>"
LIGNE1_EN_AVANT = "<dt>Financial Data &amp; Risk</dt>"
LIGNE1_EN_APRES = "<dt>Data Science &amp; AI Engineering</dt>"


REMPLACEMENTS_IA = {
    "cv-fr.html": [
        (ROLE_BANQUE, ROLE_IA),
        (PROFIL_FR_AVANT, PROFIL_FR_APRES),
        (PROJETS_FR_AVANT, PROJETS_FR_APRES),
        (NEWSRADAR_FR_AVANT, NEWSRADAR_FR_APRES),
        (DATAVIZ_FR_AVANT, DATAVIZ_FR_APRES),
        (URL_BANQUE, URL_IA),
        (DENSITE_AVANT, DENSITE_APRES),
        (LIGNE1_FR_AVANT, LIGNE1_FR_APRES),
    ],
    "cv-en.html": [
        (ROLE_BANQUE, ROLE_IA),
        (PROFIL_EN_AVANT, PROFIL_EN_APRES),
        (PROJETS_EN_AVANT, PROJETS_EN_APRES),
        (NEWSRADAR_EN_AVANT, NEWSRADAR_EN_APRES),
        (DATAVIZ_EN_AVANT, DATAVIZ_EN_APRES),
        (URL_BANQUE, URL_IA),
        (DENSITE_AVANT, DENSITE_APRES),
        (LIGNE1_EN_AVANT, LIGNE1_EN_APRES),
    ],
}
