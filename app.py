import streamlit as st
import random
import time

# Configuración de la página con Tema Oscuro forzado
st.set_page_config(
    page_title="Trivia de Economía y Empresa",
    page_icon="⚡",
    layout="centered"
)

# Estilos CSS personalizados para interfaz oscura profesional
st.markdown("""
<style>
    /* Estilos globales en modo oscuro */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    
    /* Botones de respuesta con estilo cyber */
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

    /* Caja del Cronómetro */
    div[data-testid="stMetricValue"] {
        font-size: 32px !important;
        font-weight: bold;
        color: #FF5252;
    }

    /* Tarjetas de estado */
    .stAlert {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

cuestionario = [
    {
        "pregunta": "¿Qué es la economía?",
        "correcta": "La forma en que las personas y las sociedades organizan el dinero, los bienes y el trabajo para cubrir sus necesidades.",
        "incorrectas": [
            "La ciencia exacta que calcula las matemáticas financieras de los bancos internacionales.",
            "El registro exclusivo de los impuestos y tributos que cobra el Estado.",
            "La estrategia comercial utilizada únicamente por grandes empresas multinacionales."
        ]
    },
    {
        "pregunta": "¿Qué es la economía de la empresa?",
        "correcta": "El conjunto de herramientas y criterios técnicos que se aplican dentro de un negocio para tomar decisiones y ser rentable.",
        "incorrectas": [
            "La ley gubernamental que regula el salario mínimo de los trabajadores.",
            "El departamento encargado exclusivamente de pagar la planilla y contratar personal.",
            "El estudio del comercio exterior entre diferentes países del mundo."
        ]
    },
    {
        "pregunta": "¿Cómo definirías una empresa?",
        "correcta": "Una organización que junta trabajo, capital y herramientas para fabricar bienes o dar servicios y generar ganancias.",
        "incorrectas": [
            "Un grupo de personas que se reúnen sin fines de lucro para hacer obras sociales.",
            "Un edificio físico donde solo se almacena mercancía importada.",
            "Una entidad pública encargada de administrar los recursos del Estado."
        ]
    },
    {
        "pregunta": "¿Cuáles son los factores que intervienen en la empresa?",
        "correcta": "Capital, trabajo y tierra (recursos naturales), coordinados por la gestión del negocio.",
        "incorrectas": [
            "Ventas, compras y publicidad digital.",
            "Bancos, clientes y la competencia directa.",
            "Leyes, impuestos y tratados de libre comercio."
        ]
    },
    {
        "pregunta": "¿Qué agentes intervienen en la empresa?",
        "correcta": "Internos (dueños, jefes, empleados) y externos (clientes, proveedores, bancos, competencia y Estado).",
        "incorrectas": [
            "Solo los accionistas y los gerentes generales.",
            "Únicamente los compradores e inspectores del gobierno.",
            "Los auditores externos y los consultores de marketing."
        ]
    },
    {
        "pregunta": "¿Qué diferencias hay entre entorno general y específico?",
        "correcta": "El general afecta a todos los negocios (inflación, leyes); el específico solo al sector de la empresa (clientes, competidores).",
        "incorrectas": [
            "El general se refiere al país y el específico a la oficina donde se trabaja.",
            "El general lo maneja el dueño y el específico lo manejan los empleados.",
            "El general cambia todos los días y el específico nunca cambia."
        ]
    },
    {
        "pregunta": "¿Cuántas empresas hay en Panamá aprox. y qué porcentaje representan las MIPYMES?",
        "correcta": "Alrededor de 55,000 a 60,000 empresas registradas, donde cerca del 92% al 96% son MIPYMES.",
        "incorrectas": [
            "Unos 3.3 millones de empresas, y el 99.8% son PYMES.",
            "Cerca de 500,000 empresas, y solo el 50% son PYMES.",
            "Aproximadamente 10,000 empresas, donde el 20% son MIPYMES."
        ]
    },
    {
        "pregunta": "¿Es lo mismo un empresario, un accionista y un emprendedor?",
        "correcta": "No: el emprendedor crea el negocio, el accionista pone capital/dueño de acciones, y el empresario lo gestiona.",
        "incorrectas": [
            "Sí, son exactamente tres términos sinónimos para referirse a la misma persona.",
            "No: el empresario es el empleado con más antigüedad y el accionista es el cliente principal.",
            "No: el emprendedor trabaja para el Estado y el accionista para un banco."
        ]
    },
    {
        "pregunta": "¿Cuáles son las principales funciones de la Dirección de una empresa?",
        "correcta": "Planificar la estrategia, organizar recursos, liderar al personal y controlar los resultados.",
        "incorrectas": [
            "Comprar materias primas, limpiar las instalaciones y atender el teléfono.",
            "Pagar los impuestos, tramitar licencias y otorgar préstamos.",
            "Diseñar logotipos, hacer publicaciones en redes sociales y vender."
        ]
    },
    {
        "pregunta": "¿Qué es el costo de oportunidad?",
        "correcta": "El beneficio o ganancia que se deja de recibir al elegir una opción económica en lugar de otra.",
        "incorrectas": [
            "El descuento especial que te da un proveedor por comprar al mayor.",
            "El valor total de los impuestos que se pagan al final del año fiscal.",
            "El precio de venta fijado para ganarle a la competencia."
        ]
    },
    {
        "pregunta": "¿Cuál es la relación entre la economía y sus costos?",
        "correcta": "La economía busca usar eficientemente los recursos y los costos miden el valor monetario de esos recursos.",
        "incorrectas": [
            "La economía siempre busca subir los costos para ganar más.",
            "Los costos son fijados por ley y la economía los ignora.",
            "No existe ninguna relación entre la economía y los costos."
        ]
    },
    {
        "pregunta": "¿Qué es la contabilidad financiera?",
        "correcta": "El registro estructurado de los movimientos de dinero para mostrar la salud económica a usuarios internos y externos.",
        "incorrectas": [
            "La lista de tareas diarias que deben hacer los trabajadores de planta.",
            "El archivo donde se guardan los currículums de los candidatos.",
            "El cálculo del precio final de venta al consumidor."
        ]
    },
    {
        "pregunta": "¿Cuáles son los principales objetivos de la contabilidad de costos?",
        "correcta": "Saber cuánto cuesta fabricar un producto, fijar precios, controlar gastos y evitar fugas de dinero.",
        "incorrectas": [
            "Pagar la menor cantidad de salarios posibles a los empleados.",
            "Aumentar el límite de crédito en las tarjetas de la empresa.",
            "Diseñar las campañas publicitarias de la marca."
        ]
    },
    {
        "pregunta": "¿Cuáles son las funciones económicas de una empresa industrial?",
        "correcta": "Transformar materia prima en productos terminados, generar empleo y aportar valor agregado.",
        "incorrectas": [
            "Revender productos importados sin hacerles ningún cambio.",
            "Prestar servicios financieros y otorgar préstamos personales.",
            "Transportar personas de una ciudad a otra."
        ]
    },
    {
        "pregunta": "¿Qué son los estados financieros?",
        "correcta": "Reportes contables oficiales que resumen la situación económica, deudas y ganancias en un periodo.",
        "incorrectas": [
            "Los contratos de trabajo firmados por el personal.",
            "Las facturas de luz y agua pendientes de pago.",
            "Las leyes de comercio emitidas por el Ministerio de Economía."
        ]
    },
    {
        "pregunta": "¿Qué es gasto?",
        "correcta": "Salida de dinero para mantener la operación general (luz, alquiler) que no genera retorno directo.",
        "incorrectas": [
            "La inversión en materia prima que se recupera al vender el producto.",
            "El dinero que se guarda en la cuenta de ahorros del banco.",
            "El beneficio neto que se reparte a los socios."
        ]
    },
    {
        "pregunta": "¿Qué es costo?",
        "correcta": "Inversión directa en la elaboración del producto o servicio que se recupera cuando el cliente paga por él.",
        "incorrectas": [
            "El dinero dedicado a pagar las multas del gobierno.",
            "El pago de la publicidad en televisión y radio.",
            "Cualquier pérdida involuntaria de dinero en la empresa."
        ]
    },
    {
        "pregunta": "¿Qué funciones realiza la empresa en el mercado?",
        "correcta": "Asumir riesgos, crear empleos, innovar productos y coordinar la producción para abastecer a la sociedad.",
        "incorrectas": [
            "Fijar las leyes de impuestos y regular el salario mínimo.",
            "Controlar la tasa de cambio de la moneda nacional.",
            "Prestar dinero a otros países sin cobrar intereses."
        ]
    },
    {
        "pregunta": "¿Qué es la política comercial?",
        "correcta": "El plan de acción y estrategias de ventas, precios y distribución para posicionar y vender los productos.",
        "incorrectas": [
            "Las leyes laborales que aprueba la Asamblea o el Parlamento.",
            "El código de ética interno para el vestuario de los empleados.",
            "El contrato que se firma con el arrendador del local."
        ]
    },
    {
        "pregunta": "¿Qué es el comercio internacional?",
        "correcta": "La compra y venta de mercancías, servicios o capitales entre empresas o personas de diferentes países.",
        "incorrectas": [
            "La venta de productos únicamente dentro de una misma provincia o estado.",
            "El intercambio informal de bienes entre vecinos de un mismo barrio.",
            "Las transacciones que realiza el banco central con los bancos locales."
        ]
    },
    {
        "pregunta": "¿Cuál es el objetivo principal de una empresa?",
        "correcta": "Generar utilidades para sus dueños, garantizando su supervivencia, crecimiento y la satisfacción del cliente.",
        "incorrectas": [
            "Donar todo el dinero recolectado a obras de caridad.",
            "Producir la mayor cantidad de bienes aunque nadie los compre.",
            "Evitar contratar empleados para no pagar planillas."
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre costes fijos y variables?",
        "correcta": "Los fijos no cambian según la producción (ej. alquiler); los variables suben o bajan según lo que fabriques.",
        "incorrectas": [
            "Los fijos los paga el Estado y los variables los paga el cliente final.",
            "Los fijos cambian todos los meses y los variables se mantienen igual por años.",
            "Los fijos son los gastos de publicidad y los variables son los salarios."
        ]
    },
    {
        "pregunta": "¿Qué representa el entorno empresarial?",
        "correcta": "La suma de todos los elementos internos y externos que rodean al negocio y condicionan su éxito.",
        "incorrectas": [
            "Únicamente el espacio físico o terreno donde está construida la fábrica.",
            "El organigrama con la foto de todos los jefes de la empresa.",
            "El reglamento interno de convivencia entre empleados."
        ]
    },
    {
        "pregunta": "¿Qué es la cuota de mercado?",
        "correcta": "La porción de ventas totales de un sector que está concentrada en manos de una sola empresa.",
        "incorrectas": [
            "El pago mensual que hace la empresa al banco para saldar una deuda.",
            "El precio máximo fijado por el gobierno para un producto de la canasta básica.",
            "El porcentaje de ganancia que se le da a los vendedores por cada venta."
        ]
    },
    {
        "pregunta": "¿Qué es un mercado?",
        "correcta": "El punto de encuentro (físico o virtual) donde compradores y vendedores acuerdan intercambios a un precio.",
        "incorrectas": [
            "Únicamente el supermercado de la esquina donde se compran víveres.",
            "El lugar donde el gobierno almacena las reservas de oro del país.",
            "El sistema informático donde se registran los pagos de planillas."
        ]
    },
    {
        "pregunta": "¿Qué es la competencia perfecta?",
        "correcta": "Un escenario con muchos compradores y vendedores ofreciendo productos idénticos sin que nadie fije el precio solo.",
        "incorrectas": [
            "Un mercado donde una sola empresa vende todo y no tiene competidores.",
            "Una guerra de precios agresiva donde las empresas quiebran entre sí.",
            "Un acuerdo secreto entre dos empresas para subir los precios."
        ]
    },
    {
        "pregunta": "¿Qué caracteriza a un monopolio?",
        "correcta": "Una sola empresa controla toda la oferta de un producto o servicio sin que existan alternativas directas.",
        "incorrectas": [
            "Muchas pequeñas empresas compitiendo libremente en el mercado.",
            "La prohibición total de vender productos importados.",
            "Un mercado donde el cliente decide siempre el precio."
        ]
    },
    {
        "pregunta": "¿Qué es un oligopolio?",
        "correcta": "Un mercado dominado por un grupo reducido de empresas poderosas cuyas decisiones se afectan entre sí.",
        "incorrectas": [
            "Un mercado donde cualquiera puede vender sin pagar impuestos.",
            "La venta exclusiva de productos de segunda mano.",
            "Un sector donde no existen empresas privadas, solo públicas."
        ]
    },
    {
        "pregunta": "¿Cómo funciona la ley de la oferta y la demanda?",
        "correcta": "Si hay escasez o mucha demanda el precio sube; si abunda o nadie lo busca el precio cae hasta equilibrarse.",
        "incorrectas": [
            "El precio siempre lo fija el gobierno mediante decretos semanales.",
            "A mayor precio, los clientes siempre compran más cantidad del producto.",
            "La oferta y la demanda no influyen en el precio de los bienes."
        ]
    },
    {
        "pregunta": "¿Qué es una investigación de mercados?",
        "correcta": "La recolección sistemática de datos sobre clientes, competencia y entorno para tomar decisiones informadas.",
        "incorrectas": [
            "Una inspección policial dentro de los locales comerciales.",
            "La auditoría anual que hace el fisco para verificar impuestos.",
            "El inventario físico de la mercancía guardada en bodega."
        ]
    },
    {
        "pregunta": "¿Cuál es la función de una muestra estadística?",
        "correcta": "Estudiar a un grupo pequeño pero representativo para sacar conclusiones sin encuestar a toda la población.",
        "incorrectas": [
            "Regalar productos gratis a los clientes para que opinen.",
            "Analizar el 100% de los datos de todos los habitantes del país.",
            "Comprobar si una máquina de la fábrica está defectuosa."
        ]
    },
    {
        "pregunta": "¿Qué es el mercado meta u objetivo?",
        "correcta": "El grupo específico de clientes con el perfil ideal al que la empresa dirige sus ventas y publicidad.",
        "incorrectas": [
            "La meta de ventas en dólares que debe alcanzar la empresa al mes.",
            "El país extranjero a donde se quiere exportar en el futuro.",
            "El total de la población de una ciudad sin importar su edad o gustos."
        ]
    },
    {
        "pregunta": "¿Qué diferencia hay entre investigación cualitativa y cuantitativa?",
        "correcta": "La cualitativa analiza motivos, opiniones y gustos; la cuantitativa mide datos numéricos y estadísticas.",
        "incorrectas": [
            "La cualitativa usa números y la cuantitativa usa encuestas de texto.",
            "La cualitativa es para empresas grandes y la cuantitativa para pequeñas.",
            "No hay diferencia, ambas miden únicamente la cantidad de ventas."
        ]
    },
    {
        "pregunta": "¿Qué es la segmentación de mercados?",
        "correcta": "Dividir a los consumidores en grupos más pequeños con características parecidas para ofrecerles algo adaptado.",
        "incorrectas": [
            "Cerrar sucursales de la empresa que no están generando suficientes ventas.",
            "Separar los costos de producción de los gastos administrativos.",
            "Clasificar a los proveedores según los precios que ofrecen."
        ]
    }
]

# Inicialización del Estado de Juego
if "juego_iniciado" not in st.session_state:
    st.session_state.juego_iniciado = False
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
if "respondido" not in st.session_state:
    st.session_state.respondido = False
if "opciones" not in st.session_state:
    st.session_state.opciones = []
if "tiempo_inicio" not in st.session_state:
    st.session_state.tiempo_inicio = 0

# Banner de la App
st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1200&auto=format&fit=crop", use_container_width=True)
st.title("⚡ Trivia: La Empresa y sus Aspectos Económicos")

# Barra Lateral - Desarrollador con enlace corregido
st.sidebar.title("👨‍💻 Desarrollador")
st.sidebar.markdown("**David Solís**")
st.sidebar.markdown("[📸 Sígueme en Instagram: @dav11d_s](https://instagram.com/dav11d_s)")
st.sidebar.markdown("---")
st.sidebar.caption("Plataforma interactiva de repaso académico.")

# Pantalla de Configuración Inicial
if not st.session_state.juego_iniciado:
    st.subheader("⚙️ Configura tu Partida")
    
    dificultad = st.select_slider(
        "Selecciona la Dificultad (Tiempo por pregunta):",
        options=["Fácil (20 seg)", "Medio (15 seg)", "Difícil (10 seg)"],
        value="Medio (15 seg)"
    )
    
    tiempos = {
        "Fácil (20 seg)": 20,
        "Medio (15 seg)": 15,
        "Difícil (10 seg)": 10
    }
    st.session_state.tiempo_limite = tiempos[dificultad]
    
    st.info(f"⏱️ Tendrás **{st.session_state.tiempo_limite} segundos** por cada pregunta.")
    
    if st.button("🚀 Comenzar Quiz", use_container_width=True):
        st.session_state.juego_iniciado = True
        st.session_state.preguntas = cuestionario.copy()
        random.shuffle(st.session_state.preguntas)
        st.session_state.tiempo_inicio = time.time()
        st.rerun()

# Pantalla de Preguntas / Juego Activo
else:
    total_preguntas = len(st.session_state.preguntas)

    if st.session_state.indice < total_preguntas:
        q = st.session_state.preguntas[st.session_state.indice]
        
        # Cargar opciones aleatorias por pregunta
        if not st.session_state.opciones:
            opts = [q['correcta']] + q['incorrectas']
            random.shuffle(opts)
            st.session_state.opciones = opts
            st.session_state.tiempo_inicio = time.time()

        # Cálculo dinámico del cronómetro en tiempo real
        tiempo_transcurrido = time.time() - st.session_state.tiempo_inicio
        tiempo_restante = max(0, int(st.session_state.tiempo_limite - tiempo_transcurrido))

        # Encabezado del juego y cronómetro persistente
        col_prog, col_time, col_pts = st.columns([2, 1, 1])
        with col_prog:
            st.caption(f"Pregunta {st.session_state.indice + 1} de {total_preguntas}")
            st.progress((st.session_state.indice) / total_preguntas)
        with col_time:
            st.metric(label="⏱️ Tiempo", value=f"{tiempo_restante}s")
        with col_pts:
            st.metric(label="🎯 Puntos", value=st.session_state.puntaje)

        st.markdown(f"### {q['pregunta']}")

        # Si se acaba el tiempo y no ha respondido
        if tiempo_restante == 0 and not st.session_state.respondido:
            st.session_state.respondido = True
            st.error("⏰ ¡Tiempo agotado! Se marcó como incorrecta.")

        # Generación de Botones de Opción
        for opcion in st.session_state.opciones:
            if st.button(opcion, key=f"btn_{st.session_state.indice}_{opcion}", use_container_width=True, disabled=st.session_state.respondido):
                st.session_state.respondido = True
                if opcion == q['correcta']:
                    st.success("✅ ¡Respuesta Correcta!")
                    st.session_state.puntaje += 1
                else:
                    st.error(f"❌ Incorrecto. La respuesta era: {q['correcta']}")

        # Avanzar a la siguiente pregunta
        if st.session_state.respondido:
            st.markdown("---")
            if st.button("Siguiente Pregunta ➡️", use_container_width=True):
                st.session_state.indice += 1
                st.session_state.respondido = False
                st.session_state.opciones = []
                st.rerun()

        # Bucle de refresco para actualizar el reloj cada segundo mientras no responda
        elif tiempo_restante > 0:
            time.sleep(1)
            st.rerun()

    # Pantalla Final
    else:
        st.balloons()
        st.header("🏆 ¡Cuestionario Completado!")
        
        porcentaje = (st.session_state.puntaje / total_preguntas) * 100
        
        col_res1, col_res2 = st.columns(2)
        col_res1.metric("Puntaje Final", f"{st.session_state.puntaje} / {total_preguntas}")
        col_res2.metric("Efectividad", f"{porcentaje:.1f}%")
        
        if porcentaje == 100:
            st.success("👑 ¡Dominio Absoluto! Te sabes toda la materia al 100%.")
        elif porcentaje >= 75:
            st.info("👏 ¡Excelente Rendimiento! Estás listo para el examen.")
        else:
            st.warning("📚 Buen intento. A repasar un poco más los conceptos.")

        st.markdown("---")
        if st.button("🔄 Jugar de Nuevo", use_container_width=True):
            st.session_state.clear()
            st.rerun()
