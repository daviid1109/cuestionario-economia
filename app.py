import streamlit as st
import random
import time
from gtts import gTTS
import io

# Configuración de la página
st.set_page_config(
    page_title="La Empresa y sus Aspectos Económicos",
    page_icon="📚",
    layout="centered"
)

# Estilos CSS personalizados (Modo Oscuro)
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .titulo-compacto {
        font-size: 20px !important;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 15px;
        text-align: left;
    }
    .ig-box {
        background-color: #1E222D;
        border: 1px solid #2E3440;
        border-radius: 8px;
        padding: 6px 10px;
        text-align: center;
        font-size: 14px;
        font-weight: 600;
        margin-top: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }
    .ig-box a {
        color: #00E676;
        text-decoration: none;
    }
    .stButton>button {
        background-color: #1E222D;
        color: #E0E0E0;
        border: 1px solid #2E3440;
        border-radius: 12px;
        padding: 14px 20px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #2D3342;
        border-color: #00E676;
        color: #FFFFFF;
        box-shadow: 0px 0px 10px rgba(0, 230, 118, 0.2);
    }
    .card-correcta {
        background-color: #00E676;
        color: #000000;
        border: 2px solid #00E676;
        border-radius: 12px;
        padding: 18px 22px;
        font-weight: 700;
        font-size: 17px;
        margin-bottom: 12px;
        transform: scale(1.03);
        box-shadow: 0px 0px 20px rgba(0, 230, 118, 0.5);
    }
    .card-incorrecta {
        background-color: #FF5252;
        color: #FFFFFF;
        border: 2px solid #FF5252;
        border-radius: 12px;
        padding: 16px 20px;
        font-weight: 600;
        font-size: 16px;
        margin-bottom: 12px;
        box-shadow: 0px 0px 12px rgba(255, 82, 82, 0.4);
    }
    div[data-testid="stMetricValue"] {
        font-size: 24px !important;
        font-weight: bold;
        color: #FF5252;
    }
</style>
""", unsafe_allow_html=True)

# Función para convertir texto a audio
def texto_a_audio(texto):
    tts = gTTS(text=texto, lang='es')
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp

cuestionario = [
    {
        "pregunta": "¿Qué es la economía?",
        "correcta": "La forma en que la sociedad organiza recursos escasos para cubrir necesidades humanas.",
        "incorrectas": [
            "El cálculo exclusivo de matemáticas financieras y tasas de interés en bancos privados.",
            "El sistema estatal para fiscalizar cobros de impuestos y aranceles a particulares.",
            "Las estrategias comerciales aplicadas únicamente por empresas transnacionales."
        ]
    },
    {
        "pregunta": "¿Qué es la economía de la empresa?",
        "correcta": "El conjunto de criterios técnicos aplicados dentro del negocio para optimizar decisiones.",
        "incorrectas": [
            "La legislación laboral gubernamental que fija los salarios mínimos de empleados.",
            "La gestión administrativa orientada solo al pago de nóminas y reclutamiento interno.",
            "El análisis de transacciones financieras internacionales entre bloques económicos."
        ]
    },
    {
        "pregunta": "¿Cómo definirías una empresa?",
        "correcta": "Una organización que combina factores productivos para crear bienes y generar beneficio.",
        "incorrectas": [
            "Una entidad sin fines de lucro enfocada exclusivamente al desarrollo de obras comunitarias.",
            "Un espacio físico destinado únicamente al almacenamiento de mercancía importada.",
            "Una institución gubernamental dedicada a regular la administración de recursos públicos."
        ]
    }
]

# Inicialización del Estado
if "juego_iniciado" not in st.session_state:
    st.session_state.juego_iniciado = False
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "opcion_seleccionada" not in st.session_state:
    st.session_state.opcion_seleccionada = None
if "opciones" not in st.session_state:
    st.session_state.opciones = []
if "tiempo_inicio" not in st.session_state:
    st.session_state.tiempo_inicio = 0

st.markdown('<div class="titulo-compacto">La Empresa y sus Aspectos Económicos</div>', unsafe_allow_html=True)

if not st.session_state.juego_iniciado:
    st.subheader("⚙️ Configura tu Partida")
    
    dificultad = st.select_slider(
        "Selecciona la Dificultad (Tiempo por pregunta):",
        options=["Fácil (20 seg)", "Medio (15 seg)", "Difícil (10 seg)"],
        value="Medio (15 seg)"
    )
    
    tiempos = {"Fácil (20 seg)": 20, "Medio (15 seg)": 15, "Difícil (10 seg)": 10}
    st.session_state.tiempo_limite = tiempos[dificultad]
    
    st.info(f"⏱️ Tendrás **{st.session_state.tiempo_limite} segundos** por cada pregunta.")
    
    if st.button("🚀 Comenzar", use_container_width=True):
        st.session_state.juego_iniciado = True
        st.session_state.preguntas = cuestionario.copy()
        random.shuffle(st.session_state.preguntas)
        st.session_state.tiempo_inicio = time.time()
        st.rerun()

else:
    total_preguntas = len(st.session_state.preguntas)

    if st.session_state.indice < total_preguntas:
        q = st.session_state.preguntas[st.session_state.indice]
        
        if not st.session_state.opciones:
            opts = [q['correcta']] + q['incorrectas']
            random.shuffle(opts)
            st.session_state.opciones = opts
            st.session_state.tiempo_inicio = time.time()

        tiempo_transcurrido = time.time() - st.session_state.tiempo_inicio
        tiempo_restante = max(0, int(st.session_state.tiempo_limite - tiempo_transcurrido))

        col_ig, col_pts, col_time = st.columns([1.2, 1, 1])
        with col_ig:
            st.caption("👨‍💻 Creador")
            st.markdown('''
                <div class="ig-box">
                    <a href="https://instagram.com/dav11d_s" target="_blank">@dav11d_s</a>
                </div>
            ''', unsafe_allow_html=True)
        with col_pts:
            st.metric(label="🎯 Puntos", value=st.session_state.puntaje)
        with col_time:
            st.metric(label="⏱️ Tiempo", value=f"{tiempo_restante}s")

        st.caption(f"Pregunta {st.session_state.indice + 1} de {total_preguntas}")
        st.progress((st.session_state.indice) / total_preguntas)

        st.markdown(f"### {q['pregunta']}")

        # Reproductor de voz para la pregunta
        audio_fp = texto_a_audio(q['pregunta'])
        st.audio(audio_fp, format='audio/mp3', autoplay=False)

        if tiempo_restante == 0 and not st.session_state.respondido:
            st.session_state.respondido = True
            st.session_state.opcion_seleccionada = None

        if not st.session_state.respondido:
            for opcion in st.session_state.opciones:
                if st.button(opcion, key=f"btn_{st.session_state.indice}_{opcion}", use_container_width=True):
                    st.session_state.respondido = True
                    st.session_state.opcion_seleccionada = opcion
                    if opcion == q['correcta']:
                        st.session_state.puntaje += 1
                    st.rerun()

            if tiempo_restante > 0:
                time.sleep(1)
                st.rerun()

        else:
            sel = st.session_state.opcion_seleccionada
            if sel == q['correcta']:
                st.markdown(f'<div class="card-correcta">{q["correcta"]}</div>', unsafe_allow_html=True)
            elif sel is not None:
                st.markdown(f'<div class="card-incorrecta">{sel}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="card-correcta">{q["correcta"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="card-incorrecta">⏰ ¡Tiempo Agotado!</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="card-correcta">{q["correcta"]}</div>', unsafe_allow_html=True)

            st.markdown("---")
            if st.button("Siguiente Pregunta ➡️", use_container_width=True):
                st.session_state.indice += 1
                st.session_state.respondido = False
                st.session_state.opcion_seleccionada = None
                st.session_state.opciones = []
                st.rerun()

    else:
        st.balloons()
        st.header("🏆 ¡Cuestionario Completado!")
        porcentaje = (st.session_state.puntaje / total_preguntas) * 100
        st.metric("Puntaje Final", f"{st.session_state.puntaje} / {total_preguntas}")
        if st.button("🔄 Jugar de Nuevo", use_container_width=True):
            st.session_state.clear()
            st.rerun()
