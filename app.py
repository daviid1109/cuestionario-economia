import streamlit as st
import random
import time
from gtts import gTTS
import io
import base64

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

# Función para generar audio en gTTS
def texto_a_audio(texto):
    tts = gTTS(text=texto, lang='es', slow=False)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp

# Función para reproducir el audio acelerado a 1.5x
def reproducir_audio_rapido(audio_bytes, velocidad=1.5):
    b64 = base64.b64encode(audio_bytes.read()).decode()
    md = f"""
        <audio id="audio_tag" autoplay style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
            var audio = document.getElementById("audio_tag");
            if (audio) {{
                audio.playbackRate = {velocidad};
            }}
        </script>
    """
    st.components.v1.html(md, height=0)

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
    },
    {
        "pregunta": "¿Cuáles son los factores que intervienen en la empresa?",
        "correcta": "Capital, trabajo y recursos naturales, coordinados por la dirección de la entidad.",
        "incorrectas": [
            "Estrategias de ventas, canales de distribución y campañas de publicidad digital.",
            "Entidades bancarias, clientes recurrentes y competidores directos del mercado.",
            "Normativas fiscales, impuestos municipales y acuerdos de comercio exterior."
        ]
    },
    {
        "pregunta": "¿Qué agentes intervienen en la empresa?",
        "correcta": "Agentes internos (dueños, gerentes, personal) y externos (clientes, proveedores, Estado).",
        "incorrectas": [
            "Únicamente los accionistas mayoritarios y directores ejecutivos generales.",
            "Exclusivamente los consumidores finales y los inspectores tributarios estatales.",
            "Auditores contables independientes y firmas consultoras de gestión de marca."
        ]
    },
    {
        "pregunta": "¿Qué diferencias hay entre entorno general y específico?",
        "correcta": "El general afecta a toda la economía; el específico incide solo en el sector particular.",
        "incorrectas": [
            "El general abarca el territorio nacional; el específico se limita al área administrativa.",
            "El general lo controla el fundador; el específico lo ejecutan los colaboradores.",
            "El general varía diariamente; el específico permanece inalterable en el tiempo."
        ]
    },
    {
        "pregunta": "¿Cuántas empresas hay en Panamá aprox. y qué porcentaje representan las MIPYMES?",
        "correcta": "Entre 55,000 y 60,000 empresas registradas, de las cuales el 92%-96% son MIPYMES.",
        "incorrectas": [
            "Aproximadamente 3.3 millones de negocios, de los cuales el 99.8% son grandes firmas.",
            "Alrededor de 500,000 comercios, registrando que solo el 50% pertenecen a PYMES.",
            "Cerca de 10,000 entidades, donde la presencia de las MIPYMES representa el 20%."
        ]
    },
    {
        "pregunta": "¿Es lo mismo un empresario, un accionista y un emprendedor?",
        "correcta": "No: el emprendedor crea el negocio, el accionista aporta capital y el empresario gestiona.",
        "incorrectas": [
            "Sí, corresponden a términos conceptualmente idénticos para denominar la misma figura.",
            "No: el empresario es un trabajador operativo y el accionista es el cliente habitual.",
            "No: el emprendedor es un funcionario público y el accionista labora en la banca."
        ]
    },
    {
        "pregunta": "¿Cuáles son las principales funciones de la Dirección de una empresa?",
        "correcta": "Planificar la estrategia global, organizar recursos, liderar personal y controlar la gestión.",
        "incorrectas": [
            "Adquirir inventario, mantener el aseo operativo de la planta y procesar llamadas.",
            "Liquidar tributos públicos, solicitar registros comerciales y tramitar préstamos.",
            "Elaborar identidades gráficas, gestionar redes sociales y realizar ventas directas."
        ]
    },
    {
        "pregunta": "¿Qué es el costo de oportunidad?",
        "correcta": "El rendimiento o beneficio que se renuncia al descartar una alternativa económica.",
        "incorrectas": [
            "La rebaja especial negociada con un distribuidor por volumen de compra.",
            "La carga total de impuestos devengados al cierre del ejercicio contable.",
            "El valor de venta fijado con el propósito de superar la competencia."
        ]
    },
    {
        "pregunta": "¿Cuál es la relación entre la economía y sus costos?",
        "correcta": "La economía busca el uso eficiente de recursos y los costos cuantifican ese consumo.",
        "incorrectas": [
            "La economía procura incrementar costos operacionales para maximizar la facturación.",
            "Los costos dependen exclusivamente de decretos oficiales e ignoran la economía.",
            "No existe vinculación conceptual entre el análisis económico y la estructura de costos."
        ]
    },
    {
        "pregunta": "¿Qué es la contabilidad financiera?",
        "correcta": "El sistema que registra transacciones monetarias para reflejar el estado patrimonial.",
        "incorrectas": [
            "La lista de procedimientos operativos diarios asignados a los trabajadores.",
            "El expediente donde se archivan los historiales académicos del personal.",
            "El cálculo técnico ejecutado para determinar el margen de precio al consumidor."
        ]
    },
    {
        "pregunta": "¿Cuáles son los principales objetivos de la contabilidad de costos?",
        "correcta": "Determinar costos de producción, fijar precios de venta y controlar el gasto interno.",
        "incorrectas": [
            "Reducir las remuneraciones salariales del personal operativo de la organización.",
            "Expandir la capacidad de endeudamiento bancario a través de líneas crediticias.",
            "Desarrollar planes promocionales para campañas publicitarias institucionales."
        ]
    },
    {
        "pregunta": "¿Cuáles son las funciones económicas de una empresa industrial?",
        "correcta": "Transformar materia prima en bienes finales, crear puestos de trabajo y aportar valor.",
        "incorrectas": [
            "Comercializar productos importados sin realizar modificaciones en su estructura.",
            "Ofrecer intermediación financiera e intermediar préstamos a la comunidad.",
            "Gestionar el traslado masivo de pasajeros dentro del territorio nacional."
        ]
    },
    {
        "pregunta": "¿Qué son los estados financieros?",
        "correcta": "Documentos oficiales que sintetizan la situación económica, activos y deudas de la entidad.",
        "incorrectas": [
            "Los contratos laborales suscritos entre la administración y los empleados.",
            "Los recibos de servicios públicos acumulados pendientes de cancelación.",
            "Las normativas comerciales promulgadas por las autoridades de la nación."
        ]
    },
    {
        "pregunta": "¿Qué es gasto?",
        "correcta": "Desembolso operativo para mantener la estructura general que no se recupera directamente.",
        "incorrectas": [
            "Recurso destinado a materia prima que se reabsorbe con la venta del producto.",
            "Fondo financiero mantenido en cuentas bancarias a plazo fijo institucional.",
            "El dividendo neto que se distribuye periódicamente entre los inversionistas."
        ]
    },
    {
        "pregunta": "¿Qué es costo?",
        "correcta": "Erogación vinculada directamente a la producción que se recupera mediante la venta.",
        "incorrectas": [
            "Monto económico utilizado para la cancelación de sanciones administrativas.",
            "Inversión publicitaria efectuada en medios de difusión masiva tradicionales.",
            "Cualquier quebranto financiero fortuito sufrido dentro del período fiscal."
        ]
    },
    {
        "pregunta": "¿Qué funciones realiza la empresa en el mercado?",
        "correcta": "Asumir riesgos, fomentar empleo, impulsar la innovación y coordinar la producción.",
        "incorrectas": [
            "Establecer la estructura arancelaria y fiscalizar las escalas salariales.",
            "Determinar el tipo de cambio oficial de la divisa de circulación nacional.",
            "Conceder financiamiento a instituciones extranjeras sin aplicación de interés."
        ]
    },
    {
        "pregunta": "¿Qué es la política comercial?",
        "correcta": "El conjunto de medidas estatales para regular las transacciones comerciales internas y externas.",
        "incorrectas": [
            "El estatuto interno relativo al código de vestimenta del personal corporativo.",
            "El reglamento de contrataciones para el alquiler de instalaciones comerciales.",
            "La ley de amparo laboral aprobada por la asamblea legislativa del Estado."
        ]
    },
    {
        "pregunta": "¿Qué es el comercio internacional?",
        "correcta": "El intercambio de bienes, servicios o capitales entre diferentes países o economías.",
        "incorrectas": [
            "La distribución de productos dentro de los límites de una provincia determinada.",
            "La permuta informal de artículos realizada exclusivamente entre residentes locales.",
            "Las operaciones de crédito ejecutadas entre el banco central y la banca comercial."
        ]
    },
    {
        "pregunta": "¿Cuál es el objetivo principal de una empresa?",
        "correcta": "Generar rentabilidad económica asegurando la sostenibilidad y satisfacción del cliente.",
        "incorrectas": [
            "Transferir la totalidad de ingresos monetarios a instituciones de beneficencia.",
            "Maximizar la fabricación de mercancía descartando la demanda del mercado.",
            "Prescindir de la contratación de personal para eliminar costos operativos."
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre costes fijos y variables?",
        "correcta": "Los fijos se mantienen independientes del volumen; los variables cambian según la producción.",
        "incorrectas": [
            "Los fijos son financiados por el sector público y los variables por el consumidor.",
            "Los fijos fluctúan mensualmente y los variables permanecen estables por años.",
            "Los fijos responden a gastos de mercadeo y los variables al pago de planillas."
        ]
    },
    {
        "pregunta": "¿Qué representa el entorno empresarial?",
        "correcta": "El conjunto de factores internos y externos que condicionan el desarrollo del negocio.",
        "incorrectas": [
            "El espacio físico o área geográfica sobre la cual se construye la infraestructura.",
            "La estructura gráfica que ilustra las jerarquías de los directivos corporativos.",
            "El compendio normativo de políticas de convivencia aplicable a colaboradores."
        ]
    },
    {
        "pregunta": "¿Qué es la cuota de mercado?",
        "correcta": "El porcentaje de ventas que representa una empresa frente al total de su sector.",
        "incorrectas": [
            "La comisión amortizable pagada al banco por concepto de préstamos contratados.",
            "El tope regulatorio impuesto por el Estado para productos de primera necesidad.",
            "La comisión otorgada a los representantes comerciales sobre sus transacciones."
        ]
    },
    {
        "pregunta": "¿Qué es un mercado?",
        "correcta": "El espacio físico o virtual en que compradores y vendedores negocian intercambio de bienes.",
        "incorrectas": [
            "La instalación comercial dedicada a la venta al por menor de víveres generales.",
            "La bóveda gubernamental destinada al resguardo de reservas monetarias del país.",
            "El software de gestión utilizado para la emisión automatizada de facturación."
        ]
    },
    {
        "pregunta": "¿Qué es la competencia perfecta?",
        "correcta": "Un mercado con múltiples oferentes y demandantes con productos homogéneos sin control de precio.",
        "incorrectas": [
            "Una estructura donde una firma controla la oferta total sin alternativas directas.",
            "Un conflicto tarifario destructivo que genera el quiebre masivo de competidores.",
            "Un convenio privado pactado entre empresas líderes para elevar precios de venta."
        ]
    },
    {
        "pregunta": "¿Qué caracteriza a un monopolio?",
        "correcta": "Una sola empresa controla la oferta de un bien o servicio sin competidores cercanos.",
        "incorrectas": [
            "Un entorno donde operan pequeñas empresas compitiendo de forma equitativa.",
            "La prohibición absoluta impuesta al ingreso de bienes importados al territorio.",
            "Un modelo en el cual el consumidor determina discrecionalmente los precios."
        ]
    },
    {
        "pregunta": "¿Qué es un oligopolio?",
        "correcta": "Un mercado dominado por pocas empresas cuyas decisiones influyen directamente en las demás.",
        "incorrectas": [
            "Una actividad comercial exenta por completo del pago de tributos estatales.",
            "La venta especializada y exclusiva de artículos usados en mercados locales.",
            "Un sector económico donde la propiedad pertenece únicamente a entidades públicas."
        ]
    },
    {
        "pregunta": "¿Cómo funciona la ley de la oferta y la demanda?",
        "correcta": "A mayor demanda o escasez el precio sube; ante exceso de oferta el precio tiende a bajar.",
        "incorrectas": [
            "El valor comercial de los bienes es fijado únicamente por la regulación estatal.",
            "El volumen de compra de los clientes aumenta proporcionalmente al alza de precio.",
            "La interacción entre oferta y demanda no impacta las variaciones de mercado."
        ]
    },
    {
        "pregunta": "¿Qué es una investigación de mercados?",
        "correcta": "La recolección y análisis de datos sobre consumidores y competidores para tomar decisiones.",
        "incorrectas": [
            "El procedimiento de fiscalización efectuado en instalaciones de la entidad.",
            "La revisión contable anual exigida por la administración tributaria nacional.",
            "El conteo físico periódico del stock depositado en almacenes de la firma."
        ]
    },
    {
        "pregunta": "¿Cuál es la función de una muestra estadística?",
        "correcta": "Analizar un subconjunto representativo de la población para inferir conclusiones válidas.",
        "incorrectas": [
            "Distribuir muestras sin costo a los consumidores para incentivar la opinión.",
            "Someter a estudio al 100% de los integrantes pertenecientes a una comunidad.",
            "Verificar la presencia de defectos técnicos dentro de la maquinaría de planta."
        ]
    },
    {
        "pregunta": "¿Qué es el mercado meta u objetivo?",
        "correcta": "El segmento de clientes al cual la empresa orienta prioritariamente sus productos.",
        "incorrectas": [
            "El límite proyectado de ingresos en ventas que se planifica lograr al mes.",
            "El país extranjero seleccionado prioritariamente para futuros proyectos de exportación.",
            "La totalidad de la población residente en un municipio sin distinción de perfil."
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre investigación cualitativa y cuantitativa?",
        "correcta": "La cualitativa estudia opiniones y motivaciones; la cuantitativa mide datos y estadísticas.",
        "incorrectas": [
            "La cualitativa utiliza indicadores numéricos y la cuantitativa emplea entrevistas.",
            "La cualitativa es aplicable a corporaciones y la cuantitativa a microempresas.",
            "Ambas metodologías se orientan de forma idéntica a cuantificar inventarios."
        ]
    },
    {
        "pregunta": "¿Qué es la segmentación de mercados?",
        "correcta": "Dividir el mercado en grupos homogéneos para adaptar la oferta a sus características.",
        "incorrectas": [
            "El cierre definitivo de unidades de negocio que no cumplen los márgenes mínimos.",
            "La separación contable entre costos operativos directos y gastos administrativos.",
            "La clasificación de proveedores en función de la escala de precios otorgados."
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

# Pantalla Inicial
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

# Pantalla de Juego
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

        # Reproduce la pregunta acelerada a 1.5x
        if not st.session_state.respondido:
            audio_pregunta = texto_a_audio(q['pregunta'])
            reproducir_audio_rapido(audio_pregunta, velocidad=1.5)

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
                audio_res = texto_a_audio(f"¡oooficial, esa misma es! {q['correcta']}")
                reproducir_audio_rapido(audio_res, velocidad=1.5)

            elif sel is not None:
                st.markdown(f'<div class="card-incorrecta">{sel}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="card-correcta">{q["correcta"]}</div>', unsafe_allow_html=True)
                audio_res = texto_a_audio(f"jajajaja no. La respuesta correcta es: {q['correcta']}")
                reproducir_audio_rapido(audio_res, velocidad=1.5)

            else:
                st.markdown('<div class="card-incorrecta">⏰ ¡Tiempo Agotado!</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="card-correcta">{q["correcta"]}</div>', unsafe_allow_html=True)
                audio_res = texto_a_audio(f"Se agotó el tiempo. La respuesta correcta es: {q['correcta']}")
                reproducir_audio_rapido(audio_res, velocidad=1.5)

            st.markdown("---")
            if st.button("Siguiente Pregunta ➡️", use_container_width=True):
                st.session_state.indice += 1
                st.session_state.respondido = False
                st.session_state.opcion_seleccionada = None
                st.session_state.opciones = []
                st.rerun()

    # Pantalla Final
    else:
        st.balloons()
        st.header("🏆 ¡Cuestionario Completado!")
        porcentaje = (st.session_state.puntaje / total_preguntas) * 100
        st.metric("Puntaje Final", f"{st.session_state.puntaje} / {total_preguntas}")
        
        texto_final = f"Has completado el cuestionario con un puntaje de {st.session_state.puntaje} de {total_preguntas}."
        audio_final = texto_a_audio(texto_final)
        reproducir_audio_rapido(audio_final, velocidad=1.5)

        if st.button("🔄 Jugar de Nuevo", use_container_width=True):
            st.session_state.clear()
            st.rerun()
