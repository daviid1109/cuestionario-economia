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

# Cuestionario con las 34 preguntas del documento sin errores de sintaxis
cuestionario = [
    {
        "pregunta": "¿Qué es la economía?",
        "correcta": "Es la ciencia que estudia la asignación de recursos limitados para satisfacer necesidades humanas ilimitadas.",
        "incorrectas": [
            "El estudio exclusivo de la emisión de dinero y transacciones bancarias.",
            "La ciencia encargada de controlar los precios del mercado de forma estatal.",
            "El conjunto de leyes contables que regulan a las corporaciones financieras."
        ]
    },
    {
        "pregunta": "¿Qué es la economía de la empresa?",
        "correcta": "Estudia la combinación de factores limitados para la producción de bienes y servicios a fin de maximizar beneficios.",
        "incorrectas": [
            "El sistema de auditoría tributaria gubernamental sobre los comercios.",
            "La rama jurídica encargada del cumplimiento de las normativas de trabajo.",
            "La gestión enfocada únicamente en el reclutamiento y salario de personal."
        ]
    },
    {
        "pregunta": "¿Cómo definirías una empresa?",
        "correcta": "Unidad económica de producción que combina factores bajo condición de riesgo para producir bienes y maximizar beneficios.",
        "incorrectas": [
            "Una organización estatal dedicada a la recolección de impuestos directos.",
            "Un espacio dedicado exclusivamente al resguardo de insumos importados.",
            "Una entidad comunitaria sin fines de lucro enfocada en obras públicas."
        ]
    },
    {
        "pregunta": "¿Qué factores intervienen en la empresa?",
        "correcta": "Factores humanos, factores materiales, organización y entorno.",
        "incorrectas": [
            "Campañas publicitarias, canales de venta y estrategias de marketing.",
            "Entidades bancarias, clientes ocasionales y competidores del sector.",
            "Normativas fiscales, aranceles aduaneros y registros comerciales."
        ]
    },
    {
        "pregunta": "¿Qué agentes intervienen en la empresa?",
        "correcta": "Acreedores, clientes, proveedores, dirección, personal y accionistas.",
        "incorrectas": [
            "Únicamente los socios fundadores y gerentes ejecutivos.",
            "Exclusivamente los compradores locales e inspectores fiscales.",
            "Auditores de calidad externos y consultores independientes."
        ]
    },
    {
        "pregunta": "¿Qué diferencias hay entre entorno general y específico?",
        "correcta": "El entorno general afecta a todas las empresas; el específico afecta de forma relevante a una empresa en particular.",
        "incorrectas": [
            "El general abarca el país entero y el específico la ciudad del local.",
            "El general es manejado por el dueño y el específico por los empleados.",
            "El general no varía nunca y el específico cambia todos los días."
        ]
    },
    {
        "pregunta": "Aproximadamente, ¿Cuántas empresas hay en España? ¿Qué porcentaje aproximado son PYMES?",
        "correcta": "Aproximadamente 2,88 millones de empresas, de las cuales 1,32 millones son PYMES (45%).",
        "incorrectas": [
            "Cerca de 5 millones de empresas, de las cuales el 90% son PYMES.",
            "Alrededor de 1 millón de entidades, registrando solo un 20% de PYMES.",
            "Aproximadamente 500,000 comercios, donde el 75% representan PYMES."
        ]
    },
    {
        "pregunta": "¿Es lo mismo un empresario que un accionista y que un emprendedor?",
        "correcta": "No: el empresario directivo asume riesgo profesional, el accionista riesgo patrimonial y el emprendedor suele asumir ambos al crear la firma.",
        "incorrectas": [
            "Sí, representan términos exactos para denominar el mismo cargo.",
            "No: el empresario es operario y el accionista es cliente frecuente.",
            "No: el emprendedor es servidor público y el accionista es directivo."
        ]
    },
    {
        "pregunta": "¿Cuáles son las principales funciones de la Dirección de una empresa?",
        "correcta": "Planificación, gestión, organización/coordinación y control.",
        "incorrectas": [
            "Adquisición de mercancía, aseo de planta y atención telefónica.",
            "Trámite de patentes, cobro de facturas y pago de planillas.",
            "Diseño de marca, publicidad digital y despacho de productos."
        ]
    },
    {
        "pregunta": "¿Qué es el costo de oportunidad?",
        "correcta": "El valor de otros bienes y servicios a los que se debe renunciar para obtenerlos.",
        "incorrectas": [
            "El descuento obtenido por la compra masiva de inventario.",
            "El monto global pagado por concepto de impuestos de venta.",
            "El margen bruto asignado a un producto para la venta al público."
        ]
    },
    {
        "pregunta": "¿Cuál es la relación entre la economía y sus costos?",
        "correcta": "Los costos controlan la producción de bienes/servicios y la economía estudia las fuentes de riqueza para producir.",
        "incorrectas": [
            "La economía eleva los costos para aumentar la recaudación fiscal.",
            "Los costos sustituyen las decisiones de la economía de mercado.",
            "No guardan relación alguna en la toma de decisiones contables."
        ]
    },
    {
        "pregunta": "¿Qué es la contabilidad financiera?",
        "correcta": "Técnica que produce información financiera valuada en términos monetarios sobre las operaciones de una entidad.",
        "incorrectas": [
            "Listado de tareas operativas diarias asignadas a la planilla.",
            "Manual interno para el control de inventario y bodega.",
            "Fórmula matemática para fijar el precio final de los insumos."
        ]
    },
    {
        "pregunta": "¿Cuáles son los principales objetivos de la contabilidad de costos?",
        "correcta": "Determinar costo unitario, generar información de control, aportar a presupuestos y eficientar recursos.",
        "incorrectas": [
            "Disminuir los salarios de la planilla administrativa de la empresa.",
            "Aumentar las deudas crediticias con bancos e instituciones.",
            "Crear campañas de publicidad e imagen para el consumidor final."
        ]
    },
    {
        "pregunta": "¿Cuáles son las funciones económicas de una empresa industrial?",
        "correcta": "Comprar, transformar, producir, distribuir y administrar.",
        "incorrectas": [
            "Importar mercancía terminada sin modificar su estructura.",
            "Otorgar servicios bancarios y crédito a la comunidad.",
            "Brindar transporte y logística de pasajeros a nivel nacional."
        ]
    },
    {
        "pregunta": "¿Qué son los estados financieros?",
        "correcta": "Informes derivados de la aplicación de la contabilidad a las operaciones económicas realizadas por la empresa.",
        "incorrectas": [
            "Los contratos celebrados entre la empresa y el personal laboral.",
            "Los comprobantes de pago de servicios públicos de la planta.",
            "Leyes aprobadas por el Estado en materia comercial e industrial."
        ]
    },
    {
        "pregunta": "¿Qué es gasto?",
        "correcta": "Erogación necesaria para la operación de la empresa cuyo monto afecta a los resultados.",
        "incorrectas": [
            "Inversión directa en materia prima recuperable mediante la venta.",
            "Ahorro acumulado por la empresa en cuentas bancarias a plazo.",
            "Ganancia distribuida entre los socios al cierre del periodo fiscal."
        ]
    },
    {
        "pregunta": "¿Qué es costo?",
        "correcta": "Inversión en recursos que son recuperables por los ingresos o ventas.",
        "incorrectas": [
            "Desembolso irrecuperable asignado a sanciones administrativas.",
            "Cualquier gasto operativo general destinado a la administración.",
            "Pérdida monetaria imprevista registrada en el ejercicio económico."
        ]
    },
    {
        "pregunta": "¿Cuáles son las cuatro funciones que la empresa realiza en el mercado?",
        "correcta": "Acercar oferta y demanda, realizar cálculo económico, entregar bienes a tiempo e informar mediante comunicación comercial.",
        "incorrectas": [
            "Regular impuestos, controlar salarios, fijar tasas y fiscalizar.",
            "Establecer la moneda oficial, otorgar subsidios, pedir préstamos y vender.",
            "Exportar materias primas, auditar bancos, fijar aranceles y sancionar."
        ]
    },
    {
        "pregunta": "¿Qué es la política comercial?",
        "correcta": "Conjunto de iniciativas del gobierno de un país sobre comercio internacional (importaciones y exportaciones).",
        "incorrectas": [
            "El reglamento de vestimenta e imagen corporativa del negocio.",
            "El contrato de arrendamiento firmado para el local comercial.",
            "La estrategia de la empresa para capacitar al personal de ventas."
        ]
    },
    {
        "pregunta": "¿Qué es el comercio internacional?",
        "correcta": "Proceso de intercambio de bienes y servicios entre países (importaciones y exportaciones).",
        "incorrectas": [
            "El intercambio de productos dentro de una misma provincia.",
            "La venta minorista realizada en ferias locales y municipales.",
            "Las transferencias de dinero entre bancos centrales de un país."
        ]
    },
    {
        "pregunta": "¿Cuál es el objetivo principal de una empresa?",
        "correcta": "Maximizar sus beneficios económicos, garantizar su supervivencia, crecimiento y responsabilidad social.",
        "incorrectas": [
            "Donar la totalidad de sus ganancias a instituciones benéficas.",
            "Producir mercancía sin tomar en consideración la demanda actual.",
            "Evitar la contratación de empleados para no generar egresos."
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre costes fijos y variables?",
        "correcta": "Los fijos no cambian con el nivel de producción; los variables fluctúan directamente según la cantidad producida.",
        "incorrectas": [
            "Los fijos los paga el gobierno y los variables los paga el cliente.",
            "Los fijos cambian cada mes y los variables no cambian nunca.",
            "Los fijos son de mercadeo y los variables corresponden a salarios."
        ]
    },
    {
        "pregunta": "¿Qué representa el entorno empresarial?",
        "correcta": "El conjunto de factores externos (políticos, económicos, sociales, tecnológicos) que afectan las decisiones de la organización.",
        "incorrectas": [
            "El terreno físico y la estructura sobre la cual opera el local.",
            "El organigrama que detalla las jerarquías directivas del negocio.",
            "El código de convivencia estipulado para los trabajadores."
        ]
    },
    {
        "pregunta": "¿Qué es la cuota de mercado?",
        "correcta": "Porcentaje de ventas de un producto o servicio que tiene una empresa respecto al total vendido en ese mercado.",
        "incorrectas": [
            "El pago mensual que se liquida por créditos en entidades bancarias.",
            "El limite de producción regulado por la autoridad de comercio.",
            "La comisión asignada a los vendedores por cerrar ventas directas."
        ]
    },
    {
        "pregunta": "¿Qué es un mercado?",
        "correcta": "Espacio físico o virtual donde se encuentran compradores (demanda) y vendedores (oferta) para realizar intercambios.",
        "incorrectas": [
            "Un establecimiento enfocado a la venta exclusiva de alimentos.",
            "La caja fuerte de un banco destinada al resguardo de dinero.",
            "El sistema digital utilizado para generar facturación electrónica."
        ]
    },
    {
        "pregunta": "¿Qué es la competencia perfecta?",
        "correcta": "Estructura teórica con muchos compradores y vendedores, productos idénticos, información perfecta y sin barreras.",
        "incorrectas": [
            "Mercado dominado por una sola firma que fija los precios finales.",
            "Disputa agresiva de marcas que ocasiona la quiebra del sector.",
            "Acuerdo cerrado entre competidores para fijar tarifas mínimas."
        ]
    },
    {
        "pregunta": "¿Qué caracteriza a un monopolio?",
        "correcta": "La existencia de un único vendedor que controla la totalidad de la oferta de un bien o servicio imponiendo sus precios.",
        "incorrectas": [
            "Un sector con pequeñas empresas compitiendo de forma equitativa.",
            "La prohibición total de la entrada de artículos del extranjero.",
            "Un modelo en el cual los compradores determinan las tarifas."
        ]
    },
    {
        "pregunta": "¿Qué es un oligopolio?",
        "correcta": "Un mercado dominado por un número reducido de empresas grandes que compiten e influyen en los precios.",
        "incorrectas": [
            "Un negocio exento de obligaciones fiscales e impuestos directos.",
            "La comercialización exclusiva de bienes usados dentro del local.",
            "Un sector económico cuya propiedad pertenece por completo al Estado."
        ]
    },
    {
        "pregunta": "Cómo funciona la ley de la oferta y la demanda?",
        "correcta": "Determina el precio de equilibrio; si la demanda sube el precio tiende a aumentar, si la oferta sube el precio tiende a bajar.",
        "incorrectas": [
            "El precio de los bienes es regulado por decreto gubernamental.",
            "Las compras aumentan siempre que el precio sube en el mercado.",
            "Las variaciones de la oferta no generan cambios en los precios."
        ]
    },
    {
        "pregunta": "¿Qué es una investigación de mercados?",
        "correcta": "Proceso sistemático de recolección y análisis de datos para mejorar la toma de decisiones dentro de la empresa.",
        "incorrectas": [
            "Auditoría laboral realizada a las instalaciones administrativas.",
            "Revisión de informes contables requerida por entes fiscales.",
            "Conteo físico periódico de la mercancía ubicada en la bodega."
        ]
    },
    {
        "pregunta": "¿Cuál es la función de una muestra estadística?",
        "correcta": "Estudiar a una parte representativa de la población para extraer conclusiones válidas sin encuestar a todo el mercado.",
        "incorrectas": [
            "Regalar productos a los clientes para conocer su opinión.",
            "Encuestar obligatoriamente a la totalidad de la población.",
            "Verificar defectos de fábrica en la maquinaria industrial."
        ]
    },
    {
        "pregunta": "¿Qué es el mercado meta u objetivo?",
        "correcta": "El segmento específico de consumidores al que la empresa dirige de forma prioritaria sus productos y esfuerzos.",
        "incorrectas": [
            "El monto máximo de ventas planificado para el cierre de mes.",
            "El país extranjero elegido para la exportación de mercancía.",
            "Toda la población de una ciudad sin aplicar ningún filtro."
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre investigación cualitativa y cuantitativa?",
        "correcta": "La cualitativa analiza motivaciones y percepciones; la cuantitativa mide datos numéricos y frecuencias.",
        "incorrectas": [
            "La cualitativa usa datos numéricos y la cuantitativa entrevistas.",
            "La cualitativa es para grandes empresas y la cuantitativa para pymes.",
            "Ambas metodologías se orientan a medir la cantidad de inventario."
        ]
    },
    {
        "pregunta": "¿Qué es la segmentación de mercados?",
        "correcta": "Dividir el mercado total en grupos más pequeños de consumidores que comparten características o necesidades similares.",
        "incorrectas": [
            "El cierre de sucursales que no alcanzan las metas de venta.",
            "La división de gastos administrativos y costos de producción.",
            "La clasificación de proveedores en función de sus tarifas."
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
    
    # Opciones de tiempo
    dificultad = st.select_slider(
        "Selecciona el Tiempo por pregunta:",
        options=["15 seg", "20 seg", "25 seg"],
        value="15 seg"
    )
    
    tiempos = {"15 seg": 15, "20 seg": 20, "25 seg": 25}
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
                audio_res = texto_a_audio(f"¡Correcto! {q['correcta']}")
                reproducir_audio_rapido(audio_res, velocidad=1.5)

            elif sel is not None:
                st.markdown(f'<div class="card-incorrecta">{sel}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="card-correcta">{q["correcta"]}</div>', unsafe_allow_html=True)
                audio_res = texto_a_audio(f"Incorrecto. La respuesta correcta es: {q['correcta']}")
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
