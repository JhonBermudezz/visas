"""Genera el sitio de Visas y Pasaportes Colombia.

Uso:  python3 tools/build.py

Todo el sitio sale de este archivo y de los artículos en content/blog/.
Cabecera, menú y pie de página se escriben una vez aquí y se repiten en cada página.
Para publicar un artículo nuevo basta con agregar un .html en content/blog/ y volver a ejecutar el script.
"""
import html
import json
import os
import re
from datetime import date
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Datos del negocio (reemplazar los marcados como pendientes antes de publicar)
# ---------------------------------------------------------------------------
BRAND = 'Visas y Pasaportes Colombia'
BRAND_SHORT = 'Visas y Pasaportes'
SITE = 'https://jhonbermudezz.github.io/visas'      # dominio definitivo: pendiente
PHONE = '+57 300 000 0000'                           # pendiente
PHONE_TEL = '+573000000000'                          # pendiente
WHATSAPP = '573000000000'                            # pendiente, sin + ni espacios
EMAIL = 'contacto@visasypasaportes.com.co'           # pendiente
ADDRESS = 'Carrera 45, Bogotá'                       # número exacto pendiente
CITY = 'Bogotá, Colombia'
HOURS = 'Lunes a viernes, 8:00 a. m. a 5:00 p. m.'   # pendiente
HOURS_SHORT = 'Lun a vie · 8:00 a 17:00'
INSTAGRAM = 'https://www.instagram.com/'             # pendiente
TIKTOK = 'https://www.tiktok.com/'                   # pendiente
SEMANA_URL = ''                                      # enlace al artículo de Semana: pendiente
MAP_QUERY = 'Carrera 45, Bogotá, Colombia'
YEAR = date.today().year

FONTS = ('https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;600;700'
         '&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap')
FLAGS = 'https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css'


def wa(text):
    return f'https://wa.me/{WHATSAPP}?text={quote(text)}'


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------------------
# Íconos (un solo trazo, dibujados para este sitio)
# ---------------------------------------------------------------------------
SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.43 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.17-3.48-8.41"/></symbol>
  <symbol id="i-ig" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/></g><circle cx="17.4" cy="6.6" r="1.2" fill="currentColor"/></symbol>
  <symbol id="i-tt" viewBox="0 0 24 24"><path fill="currentColor" d="M12.53.02C13.84 0 15.14.01 16.44 0c.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M5 3.5h3.2l1.6 4.2-2.1 1.4a11 11 0 0 0 7.2 7.2l1.4-2.1 4.2 1.6V19a1.6 1.6 0 0 1-1.6 1.6A16.5 16.5 0 0 1 3.4 5.1 1.6 1.6 0 0 1 5 3.5z"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="m3.5 6 8.5 7 8.5-7"/></g></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-6.5-6.1-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 14.9 12 21 12 21z"/><circle cx="12" cy="9.8" r="2.4"/></g></symbol>
  <symbol id="i-clock" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></g></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M4 12h15m-5-5.5L19.5 12 14 17.5"/></symbol>
  <symbol id="i-down" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="m6 9 6 6 6-6"/></symbol>
  <symbol id="i-doc" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M6 2.8h8.2L19 7.6V21.2H6z"/><path d="M14 2.8V8h5M9 12.5h7M9 16h7"/></g></symbol>
  <symbol id="i-card" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2.8" y="5.5" width="18.4" height="13" rx="1.5"/><path d="M2.8 9.8h18.4M6.5 15h4"/></g></symbol>
</svg>'''


def icon(name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true"><use href="#i-{name}"></use></svg>'


ARROW = icon('arrow')

# ---------------------------------------------------------------------------
# Fotografías (todas de colecciones abiertas; créditos en assets/credits.json)
# ---------------------------------------------------------------------------
PHOTOS = {
    'bogota': ('Cerros orientales de Bogotá con la ciudad al pie', 1516, 1137, 'Bogotá'),
    'capitolio': ('Fachada oeste del Capitolio de Estados Unidos en Washington D. C.', 1920, 681, 'Washington D. C.'),
    'westminster': ('Palacio de Westminster a orillas del Támesis, Londres', 1920, 1440, 'Londres'),
    'ottawa': ('Torre de la Paz del Parlamento de Canadá en Ottawa', 1920, 1440, 'Ottawa'),
    'sidney': ('Ópera de Sídney de noche, Australia', 1920, 1061, 'Sídney'),
    'petronas': ('Torres Petronas vistas desde abajo, Kuala Lumpur', 1920, 1280, 'Kuala Lumpur'),
    'salidas': ('Tablero de salidas internacionales en un aeropuerto', 1920, 1280, 'Aeropuerto de Melbourne'),
    'sellos': ('Sellos de entrada y salida en las páginas de un pasaporte', 1920, 1293, 'Sellos migratorios'),
    'taxi': ('Taxi amarillo en la avenida El Dorado, Bogotá', 1920, 1440, 'Bogotá'),
    'candelaria': ('Calle empedrada del barrio La Candelaria, Bogotá', 1794, 1200, 'Bogotá'),
}
CREDIT_KEYS = {'west-front': 'capitolio', 'westminster': 'westminster', 'ottawa': 'ottawa', 'sydney': 'sidney', 'petronas': 'petronas',
               'cerros': 'bogota', 'melbourne': 'salidas', 'myanmar': 'sellos', 'taxi': 'taxi', 'candelaria': 'candelaria'}


def img(R, key, cls='', eager=False, sizes='100vw', alt=None):
    a, w, h, _ = PHOTOS[key]
    alt = a if alt is None else alt
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return (f'<img{c} src="{R}assets/img/{key}.webp" srcset="{R}assets/img/{key}-sm.webp 960w, {R}assets/img/{key}.webp {w}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}" {load}>')


# ---------------------------------------------------------------------------
# Servicios
# ---------------------------------------------------------------------------
US_SUBS = [
    {
        'slug': 'primera-vez', 'name': 'Primera vez', 'menu': 'Visa por primera vez',
        'h1': ['Visa americana', 'por primera vez'],
        'title': 'Visa americana por primera vez en Bogotá',
        'desc': 'Asesoría para pedir la visa americana de turismo por primera vez desde Bogotá: DS-160, pago, citas y preparación para la entrevista.',
        'lead': 'Te ayudamos a pedir la visa de turismo B1/B2 desde Bogotá: formulario DS-160, pago de la tarifa, citas y preparación para la entrevista.',
        'short': 'Formulario DS-160, citas y preparación para la entrevista.',
        'help': ['Revisamos tu perfil y el motivo del viaje antes de empezar.',
                 'Diligenciamos contigo el DS-160 con información coherente y verificable.',
                 'Te guiamos en el pago de la tarifa consular y en la programación de las citas.',
                 'Te preparamos para la entrevista con las preguntas que suelen hacer.'],
        'docs': ['Pasaporte vigente.',
                 'Fotografía digital reciente con las especificaciones del Departamento de Estado.',
                 'Soportes de arraigo: certificado laboral o de ingresos, extractos bancarios, propiedades o estudios.',
                 'Información de tus viajes anteriores.',
                 'Itinerario tentativo del viaje.'],
        'times': 'La espera para la cita la define la Embajada y cambia durante el año; al empezar te mostramos la disponibilidad del momento. La tarifa consular se paga directamente al Departamento de Estado y nuestro honorario se paga aparte.',
        'note': 'Ningún asesor puede garantizar la aprobación. En la entrevista cuenta que tus respuestas sean claras y coincidan con lo que declaraste en el formulario.',
    },
    {
        'slug': 'renovacion', 'name': 'Renovación', 'menu': 'Renovación de visa',
        'h1': ['Renovación de', 'visa americana'],
        'title': 'Renovación de visa americana desde Colombia',
        'desc': 'Renueva tu visa americana desde Bogotá: revisamos si aplicas sin entrevista, actualizamos el DS-160 y programamos las citas.',
        'lead': 'Si tu visa venció o está por vencer, revisamos si tu caso puede tramitarse sin entrevista o si debes presentarla, y preparamos la solicitud completa.',
        'short': 'Con o sin entrevista, según las condiciones vigentes.',
        'help': ['Verificamos si cumples las condiciones vigentes para renovar sin entrevista.',
                 'Actualizamos el DS-160 con tus datos actuales.',
                 'Programamos las citas y, si aplica, el envío de documentos.',
                 'Hacemos seguimiento hasta la entrega del pasaporte.'],
        'docs': ['Pasaporte vigente y pasaporte con la visa anterior.',
                 'Fotografía digital reciente.',
                 'Soportes de arraigo actualizados.',
                 'Información de los viajes que hiciste con la visa anterior.'],
        'times': 'Los tiempos dependen de la modalidad que te corresponda y de la agenda de la Embajada. La tarifa consular se paga directamente al Departamento de Estado.',
        'note': 'Las condiciones para renovar sin entrevista las fija el Departamento de Estado y han cambiado varias veces. Siempre las validamos con la información oficial del momento.',
    },
    {
        'slug': 'visa-revocada', 'name': 'Visa revocada', 'menu': 'Visa revocada',
        'h1': ['Visa americana', 'revocada'],
        'title': 'Visa americana revocada: qué hacer',
        'desc': 'Si te revocaron la visa americana, analizamos la notificación y tu historial para preparar una nueva solicitud con soportes coherentes.',
        'lead': 'Si te notificaron la revocatoria de tu visa, analizamos la notificación y tu historial para preparar una nueva solicitud con soportes coherentes.',
        'short': 'Análisis de la revocatoria y nueva solicitud.',
        'help': ['Leemos contigo la notificación y lo que dice sobre la causa.',
                 'Revisamos tu historial de viajes y de solicitudes anteriores.',
                 'Evaluamos el momento y la forma adecuada de volver a aplicar.',
                 'Preparamos el nuevo DS-160 y la entrevista.'],
        'docs': ['Notificación de revocatoria (correo o carta).',
                 'Pasaporte con la visa revocada.',
                 'Historial de viajes a Estados Unidos.',
                 'Soportes de arraigo actualizados.'],
        'times': 'Primero analizamos el caso; el tiempo de la nueva solicitud depende de la agenda de la Embajada. La tarifa consular se paga directamente al Departamento de Estado.',
        'note': 'Una visa revocada no se reactiva: hay que presentar una solicitud nueva. Si la revocatoria tiene que ver con un asunto migratorio o judicial, te lo decimos con claridad y, si hace falta, te remitimos a un abogado.',
    },
    {
        'slug': 'visa-perdida', 'name': 'Visa perdida o robada', 'menu': 'Visa perdida o robada',
        'h1': ['Visa americana', 'perdida o robada'],
        'title': 'Visa americana perdida o robada',
        'desc': 'Perdiste el pasaporte con la visa americana o te lo robaron: qué denunciar, a quién avisar y cómo volver a solicitarla.',
        'lead': 'Si perdiste el pasaporte con la visa o te lo robaron, te indicamos qué denunciar, a quién avisar y cómo volver a solicitar la visa.',
        'short': 'Denuncia, reporte a la Embajada y nueva solicitud.',
        'help': ['Te orientamos para presentar la denuncia de pérdida o hurto.',
                 'Te indicamos cómo reportar la visa perdida ante la Embajada.',
                 'Si también perdiste el pasaporte, te explicamos cómo pedir uno nuevo.',
                 'Preparamos la nueva solicitud de visa.'],
        'docs': ['Denuncia de pérdida o hurto.',
                 'Pasaporte nuevo o vigente.',
                 'Copia de la visa perdida, si la tienes.',
                 'Fotografía digital reciente.'],
        'times': 'Primero se tramita el pasaporte nuevo si hace falta; después la visa sigue el proceso habitual de la Embajada.',
        'note': 'La visa perdida no se reemplaza: se tramita una nueva. Si estaba vigente, reportarla evita que otra persona la use.',
    },
]

COUNTRIES = [
    {
        'slug': 'visa-reino-unido', 'country': 'Reino Unido', 'flag': 'gb', 'photo': 'westminster', 'cls': 'uk',
        'h1': ['Visa de turismo', 'para Reino Unido'],
        'title': 'Visa de turismo para Reino Unido desde Colombia',
        'desc': 'Visa de visitante para Reino Unido: solicitud en línea, soportes financieros y cita biométrica en Bogotá, con asesoría paso a paso.',
        'lead': 'Los colombianos necesitan visa de visitante para viajar al Reino Unido. Preparamos la solicitud en línea, los soportes y la cita biométrica en Bogotá.',
        'short': 'Visa de visitante, solicitud en línea y biometría.',
        'help': ['Revisamos el propósito y la duración del viaje.',
                 'Diligenciamos la solicitud en línea del Gobierno británico.',
                 'Organizamos los soportes financieros y de arraigo, con traducción cuando aplica.',
                 'Te guiamos en la cita de biometría en el centro de solicitudes.'],
        'docs': ['Pasaporte vigente.', 'Extractos bancarios recientes.', 'Certificado laboral o de ingresos.',
                 'Reservas o itinerario del viaje.', 'Carta de invitación, si te hospeda alguien.'],
        'times': 'El Gobierno británico publica tiempos de decisión de referencia que varían según la temporada. La tarifa de la visa se paga en línea al Gobierno británico.',
        'note': 'Los documentos en español suelen necesitar traducción. Te decimos cuáles antes de que pagues una traducción que no hace falta.',
    },
    {
        'slug': 'visa-canada', 'country': 'Canadá', 'flag': 'ca', 'photo': 'ottawa', 'cls': 'ca',
        'h1': ['Visa de turismo', 'para Canadá'],
        'title': 'Visa de turismo para Canadá desde Colombia',
        'desc': 'Visa de visitante para Canadá: revisamos si aplicas a visa o a eTA, diligenciamos la solicitud en línea y te guiamos en la biometría.',
        'lead': 'Preparamos tu solicitud de visa de visitante en la cuenta en línea del Gobierno de Canadá, con soportes ordenados y la cita de biometría.',
        'short': 'Visa de visitante o eTA, según tu caso.',
        'help': ['Revisamos si tu caso corresponde a visa de visitante o a autorización electrónica de viaje (eTA).',
                 'Creamos y diligenciamos la solicitud en línea.',
                 'Organizamos los soportes de arraigo y solvencia.',
                 'Te guiamos en la toma de datos biométricos.'],
        'docs': ['Pasaporte vigente.', 'Extractos bancarios y soportes de ingresos.', 'Certificado laboral o de estudios.',
                 'Historial de viajes.', 'Itinerario y, si aplica, carta de invitación.'],
        'times': 'El Gobierno de Canadá publica los tiempos de procesamiento vigentes y los actualiza con frecuencia. Las tarifas de visa y biometría se pagan en línea al Gobierno de Canadá.',
        'note': 'La solicitud se evalúa por escrito: los soportes tienen que contar tu caso sin que nadie los explique. Por eso los revisamos uno por uno.',
    },
    {
        'slug': 'visa-australia', 'country': 'Australia', 'flag': 'au', 'photo': 'sidney', 'cls': 'au',
        'h1': ['Visa de turismo', 'para Australia'],
        'title': 'Visa de turismo para Australia desde Colombia',
        'desc': 'Visa de visitante para Australia (subclase 600): solicitud en ImmiAccount con soportes completos y en orden.',
        'lead': 'Gestionamos la visa de visitante (subclase 600) en ImmiAccount, la plataforma del Gobierno australiano, con soportes completos y en orden.',
        'short': 'Visa de visitante subclase 600 en línea.',
        'help': ['Revisamos tu perfil y el plan de viaje.',
                 'Creamos la cuenta y diligenciamos la solicitud en ImmiAccount.',
                 'Organizamos y cargamos los soportes.',
                 'Te acompañamos si el Gobierno pide información adicional o exámenes.'],
        'docs': ['Pasaporte vigente.', 'Extractos bancarios recientes.', 'Certificado laboral o de ingresos.',
                 'Itinerario y reservas.', 'Soportes de vínculos con Colombia.'],
        'times': 'El Gobierno australiano publica tiempos de procesamiento de referencia. La tarifa de la visa se paga en línea al presentar la solicitud.',
        'note': 'En algunos casos el Gobierno australiano pide datos biométricos o exámenes médicos después de presentar la solicitud. Si te los piden, te guiamos.',
    },
    {
        'slug': 'visa-malasia', 'country': 'Malasia', 'flag': 'my', 'photo': 'petronas', 'cls': 'my',
        'h1': ['Visa de turismo', 'para Malasia'],
        'title': 'Visa de turismo para Malasia desde Colombia',
        'desc': 'Requisitos de entrada a Malasia para colombianos: te confirmamos si necesitas visa o solo el registro digital de llegada, y gestionamos la solicitud.',
        'lead': 'Te confirmamos qué exige Malasia para tu viaje según la duración de la estadía, y gestionamos la solicitud o el registro cuando aplica.',
        'short': 'Requisitos de entrada y registro digital de llegada.',
        'help': ['Confirmamos los requisitos de entrada vigentes para tu caso.',
                 'Gestionamos la solicitud de visa cuando tu viaje la requiere.',
                 'Te guiamos en el registro digital de llegada (MDAC).',
                 'Revisamos los soportes que pueden pedirte al ingresar.'],
        'docs': ['Pasaporte con vigencia mínima de seis meses.', 'Tiquete de regreso o de salida del país.',
                 'Reserva de alojamiento.', 'Soportes de solvencia económica.'],
        'times': 'El registro digital de llegada se hace en línea pocos días antes del viaje. Si tu caso requiere visa, te indicamos el tiempo de respuesta vigente.',
        'note': 'Los requisitos de entrada pueden cambiar. Los validamos con las fuentes oficiales de Malasia antes de tu viaje.',
    },
]

US = {
    'slug': 'visa-estados-unidos', 'country': 'Estados Unidos', 'flag': 'us', 'photo': 'capitolio', 'cls': 'us',
    'title': 'Visa americana en Bogotá: asesoría completa',
    'desc': 'Asesoría para la visa americana desde Bogotá: primera vez, renovación, visa revocada y visa perdida o robada.',
}

# Valores de referencia para el armador de consultas (los precios llegan del cliente)
PLANNER = {
    'us': {'country': 'Estados Unidos', 'flag': 'us', 'options': [
        {'id': s['slug'], 'label': s['name'], 'docs': s['docs'][:4], 'url': f'servicios/visa-estados-unidos/{s["slug"]}/'} for s in US_SUBS]},
}
for c in COUNTRIES:
    PLANNER[c['flag']] = {'country': c['country'], 'flag': c['flag'], 'options': [
        {'id': 'turismo', 'label': 'Turismo', 'docs': c['docs'][:4], 'url': f'servicios/{c["slug"]}/'}]}


# ---------------------------------------------------------------------------
# Documentos y políticas
# ---------------------------------------------------------------------------
LEGAL = [
    ('politica-de-tratamiento-de-datos', 'Tratamiento de datos personales', 'Cómo recogemos, usamos y protegemos tu información (Ley 1581 de 2012).'),
    ('politica-de-manejo-de-casos', 'Manejo de casos', 'Qué hacemos en cada caso, qué decides tú y qué decide el consulado.'),
    ('terminos-y-condiciones', 'Términos y condiciones', 'Las reglas del servicio de asesoría y del uso de este sitio.'),
    ('politica-de-reembolsos', 'Reembolsos', 'En qué casos devolvemos el valor de la asesoría y cómo pedirlo.'),
    ('pqrs', 'PQRS', 'Peticiones, quejas, reclamos y sugerencias: cómo radicarlas y en qué plazo respondemos.'),
]


def docs_list(R):
    out = []
    for slug, name, sub in LEGAL:
        out.append(f'<a class="doc-link" href="{R}{slug}/">{icon("doc")}<div><strong>{name}</strong><span>{sub}</span></div>{icon("arrow", "go")}</a>')
    return '\n          '.join(out)


# ---------------------------------------------------------------------------
# Blog: lee content/blog/*.html (encabezado entre líneas ---)
# ---------------------------------------------------------------------------
MONTHS = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']


def fdate(iso):
    y, m, d = (int(x) for x in iso.split('-'))
    return f'{d} de {MONTHS[m - 1]} de {y}'


def load_posts():
    posts = []
    folder = os.path.join(ROOT, 'content', 'blog')
    for name in sorted(os.listdir(folder)):
        if not name.endswith('.html'):
            continue
        raw = open(os.path.join(folder, name), encoding='utf-8').read()
        _, head, body = raw.split('---', 2)
        meta = {}
        for line in head.strip().splitlines():
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
        meta['body'] = body.strip()
        meta['slug'] = name[:-5]
        meta.setdefault('h1', meta['title'])
        meta['toc'] = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
        posts.append(meta)
    posts.sort(key=lambda p: (p.get('featured') == 'si', p['date']), reverse=True)
    return posts


POSTS = load_posts()
CATEGORIES = sorted({p['category'] for p in POSTS})


# ---------------------------------------------------------------------------
# Cabecera, menú y pie
# ---------------------------------------------------------------------------
def head(R, title, desc, path, ld=None, noindex=False):
    full = f'{title} | {BRAND_SHORT}' if len(title) + len(BRAND_SHORT) <= 57 else title
    url = f'{SITE}/{path}'
    lds = ''.join(f'\n  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (ld or []))
    robots = '\n  <meta name="robots" content="noindex">' if noindex else ''
    return f'''<!doctype html>
<html lang="es-CO">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(full)}</title>
  <meta name="description" content="{esc(desc)}">{robots}
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#0c1f4d">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_CO">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:title" content="{esc(full)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/og.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" href="{R}assets/img/favicon.png">
  <link rel="apple-touch-icon" href="{R}assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS}" rel="stylesheet">
  <link href="{FLAGS}" rel="stylesheet">
  <link rel="stylesheet" href="{R}assets/css/styles.css">
  <script>document.documentElement.classList.add('js')</script>{lds}
</head>'''


def flag(code, extra=''):
    return f'<span class="fi fi-{code}{extra}" aria-hidden="true"></span>'


def mega(R):
    subs = ''.join(f'<li><a href="{R}servicios/visa-estados-unidos/{s["slug"]}/">{s["menu"]}</a></li>' for s in US_SUBS)
    dest = ''.join(
        f'<a href="{R}servicios/{c["slug"]}/">{flag(c["flag"])}<span>{c["country"]}<small>Visa de turismo</small></span></a>'
        for c in COUNTRIES)
    return f'''<div class="mega" id="menu-servicios">
              <div class="mega__group">
                <h3>{flag("us")}<a href="{R}servicios/visa-estados-unidos/">Estados Unidos</a></h3>
                <ul class="mega__sub">{subs}</ul>
              </div>
              <div class="mega__dest">{dest}</div>
              <p class="mega__all"><span>Procesos de visa internacional</span><a class="more" href="{R}servicios/">Ver todos los servicios {ARROW}</a></p>
            </div>'''


NAV = [('', 'Inicio'), ('servicios/', 'Servicios'), ('nosotros/', 'Nosotros'), ('blog/', 'Blog'), ('contacto/', 'Contacto')]


def header(R, active):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if active == href else ''
        if href == 'servicios/':
            items.append(f'''<li class="has-menu">
            <a class="nav__link" href="{R}{href}"{cur} aria-haspopup="true" aria-expanded="false" aria-controls="menu-servicios">{label} {icon("down")}</a>
            {mega(R)}
          </li>''')
        else:
            items.append(f'<li><a class="nav__link" href="{R}{href}"{cur}>{label}</a></li>')
    msubs = ''.join(f'<li><a class="sub" href="{R}servicios/visa-estados-unidos/{s["slug"]}/">{s["menu"]}</a></li>' for s in US_SUBS)
    mdest = ''.join(f'<li><a href="{R}servicios/{c["slug"]}/">{flag(c["flag"])}{c["country"]}</a></li>' for c in COUNTRIES)
    return f'''<body>
  {SPRITE}
  <a class="skip" href="#main">Saltar al contenido</a>
  <div class="topbar">
    <div class="wrap topbar__inner">
      <p class="topbar__info"><span>{CITY}</span><span>{HOURS_SHORT}</span></p>
      <div class="topbar__links">
        <a href="tel:{PHONE_TEL}">{icon("phone")}{PHONE}</a>
        <a class="hide-sm" href="mailto:{EMAIL}">{icon("mail")}{EMAIL}</a>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{icon("ig")}</a>
        <a href="{TIKTOK}" target="_blank" rel="noopener" aria-label="TikTok">{icon("tt")}</a>
      </div>
    </div>
  </div>
  <header class="header" id="top">
    <div class="wrap header__inner">
      <a class="logo" href="{R or './'}" aria-label="{BRAND}, inicio"><img src="{R}assets/img/logo.webp" alt="{BRAND}" width="640" height="274"></a>
      <nav class="nav" aria-label="Principal">
        <ul class="nav__list">
          {"".join(items)}
        </ul>
      </nav>
      <div class="header__cta">
        <a class="btn btn--line btn--sm" href="{wa("Hola, quiero información sobre un trámite de visa.")}" target="_blank" rel="noopener" data-track="whatsapp">{icon("wa")}WhatsApp</a>
        <a class="btn btn--primary btn--sm" href="{R}#consulta">Solicitar asesoría</a>
      </div>
      <button class="burger" type="button" aria-expanded="false" aria-controls="menu-movil" aria-label="Abrir menú"><span></span><span></span></button>
    </div>
  </header>
  <div class="mobile-menu" id="menu-movil" hidden>
    <ul>
      <li><a href="{R or './'}">Inicio</a></li>
      <li><details><summary>Servicios {icon("down")}</summary>
        <ul>
          <li><a href="{R}servicios/visa-estados-unidos/">{flag("us")}Estados Unidos</a></li>
          {msubs}
          {mdest}
          <li><a href="{R}servicios/">Todos los servicios</a></li>
        </ul></details></li>
      <li><a href="{R}nosotros/">Nosotros</a></li>
      <li><a href="{R}blog/">Blog</a></li>
      <li><a href="{R}contacto/">Contacto</a></li>
    </ul>
    <div class="actions">
      <a class="btn btn--primary" href="{R}#consulta">Solicitar asesoría</a>
      <a class="btn btn--wa" href="{wa("Hola, quiero información sobre un trámite de visa.")}" target="_blank" rel="noopener">{icon("wa")}Escribir por WhatsApp</a>
    </div>
  </div>
  <main id="main">'''


def footer(R):
    svc = ''.join(f'<li><a href="{R}servicios/{c["slug"]}/">Visa {c["country"]}</a></li>' for c in [US] + COUNTRIES)
    legal = ''.join(f'<li><a href="{R}{s}/">{n}</a></li>' for s, n, _ in LEGAL[:4])
    msg = 'Hola, quiero información sobre un trámite de visa.'
    return f'''
  </main>

  <footer class="footer on-navy">
    <div class="wrap">
      <div class="footer__name">
        <img src="{R}assets/img/mark-512.png" alt="" width="512" height="512" loading="lazy">
        <p>Visas y Pasaportes <span>Colombia</span></p>
      </div>
      <div class="footer__row">
        <div class="footer__places">
          <a href="{wa(msg)}" target="_blank" rel="noopener">WhatsApp {PHONE}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
          <a href="{R}contacto/#ubicacion">{ADDRESS}</a>
          <p>{HOURS}</p>
          <div class="socials" style="margin-top:1rem">
            <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{icon("ig")}</a>
            <a href="{TIKTOK}" target="_blank" rel="noopener" aria-label="TikTok">{icon("tt")}</a>
          </div>
        </div>
        <div class="footer__cols">
          <div><h2>Servicios</h2><ul>{svc}</ul></div>
          <div><h2>Empresa</h2><ul><li><a href="{R}nosotros/">Nosotros</a></li><li><a href="{R}blog/">Blog</a></li><li><a href="{R}contacto/">Contacto</a></li><li><a href="{R}pqrs/">PQRS</a></li></ul></div>
          <div><h2>Legal</h2><ul>{legal}</ul></div>
        </div>
      </div>
      <p class="footer__notice"><strong>Aviso importante.</strong> Somos una empresa privada de asesoría migratoria. No somos una embajada, un consulado ni una entidad del Gobierno. Las tarifas consulares se pagan directamente a cada entidad y la decisión sobre tu visa es siempre del consulado.</p>
      <div class="footer__legal">
        <p>© {YEAR} {BRAND}. Pagos en línea con ePayco.</p>
        <a href="#top">Volver arriba</a>
      </div>
      <p class="footer__credits">Fotografías de colecciones abiertas con licencia libre. <a href="{R}creditos/">Ver créditos</a>.</p>
    </div>
  </footer>

  <div class="float">
    <a class="float__call" href="tel:{PHONE_TEL}" aria-label="Llamar">{icon("phone")}</a>
    <a class="float__wa" href="{wa(msg)}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp" data-track="whatsapp">{icon("wa")}<span>Escríbenos</span></a>
  </div>

  <script src="{R}assets/js/main.js" defer></script>
</body>
</html>
'''


def crumbs(R, trail):
    parts = [f'<a href="{R or "./"}">Inicio</a>']
    for href, label in trail[:-1]:
        parts.append(f'<span aria-hidden="true">›</span><a href="{R}{href}">{label}</a>')
    parts.append(f'<span aria-hidden="true">›</span><span aria-current="page">{trail[-1][1]}</span>')
    return f'<nav class="crumbs" aria-label="Migas de pan">{"".join(parts)}</nav>'


def breadcrumb_ld(trail):
    items = [{'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': f'{SITE}/'}]
    for i, (href, label) in enumerate(trail, start=2):
        items.append({'@type': 'ListItem', 'position': i, 'name': label, 'item': f'{SITE}/{href}'})
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}


def lines(parts, tag='h1', cls='display lines', idattr=''):
    inner = ''.join(f'<span class="line"><span data-line style="--i:{i}">{p}</span></span>' for i, p in enumerate(parts))
    return f'<{tag} class="{cls}"{idattr}>{inner}</{tag}>'


def inner_hero(R, trail, h1_lines, lead, side='', actions='', photo=None, h1=None, photo_alt=None):
    band = f'<div class="band">{img(R, photo, eager=True, alt=photo_alt)}</div>\n    ' if photo else ''
    title = lines(h1_lines) if h1_lines else f'<h1 class="display display--long">{h1}</h1>'
    acts = f'<div class="actions">{actions}</div>' if actions else ''
    return f'''{band}<section class="page-hero">
      <div class="wrap">
        {crumbs(R, trail)}
        <div class="axis">
          <div class="axis__side page-hero__side">{side}</div>
          <div class="axis__main">
            {title}
            <p class="lead">{lead}</p>
            {acts}
          </div>
        </div>
      </div>
    </section>'''


def close_band(R, line='¿Tienes una cita cerca o una visa por renovar? Escríbenos y revisamos tu caso.'):
    return f'''
    <section class="section section--navy on-navy" aria-labelledby="hablemos">
      <div class="wrap close" data-reveal>
        <p class="close__line">{line}</p>
        <figure class="close__photo shutter" data-shutter>{img(R, "bogota", sizes="176px", alt="Bogotá, sede de nuestra oficina")}</figure>
        <div class="close__links">
          <h2 id="hablemos">Hablemos</h2>
          <a href="{wa("Hola, quiero que revisen mi caso de visa.")}" target="_blank" rel="noopener" data-track="whatsapp">WhatsApp {PHONE}</a>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
          <p class="small">{ADDRESS} · {HOURS}</p>
        </div>
      </div>
    </section>'''


def docs_section(R, title='Documentos y políticas', sub='Antes de pagar, conoce cómo tratamos tus datos, cómo manejamos cada caso y en qué condiciones hay reembolso.'):
    return f'''
    <section class="section" aria-labelledby="politicas">
      <div class="wrap split" data-reveal>
        <div><h2 class="head" id="politicas">{title}</h2><p>{sub}</p></div>
        <div class="docs">
          {docs_list(R)}
        </div>
      </div>
    </section>'''


def post_card(R, p, h='h3'):
    return f'''<a class="post-card" href="{R}blog/{p["slug"]}/" data-cat="{esc(p["category"])}">
            <div class="post-card__img">{img(R, p["image"], sizes="(max-width: 600px) 100vw, 33vw", alt=p.get("image_alt"))}</div>
            <{h}>{p["h1"]}</{h}>
            <p>{p["desc"]}</p>
            <p class="post-meta"><span class="tag">{p["category"]}</span><span>Actualizado el {fdate(p["date"])}</span></p>
          </a>'''


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)
    return path


PAGES = []


def page(path, title, desc, body, active='', ld=None, noindex=False, file=None, base=None):
    depth = path.count('/')
    R = base if base is not None else '../' * depth
    out = file or (path + 'index.html' if path else 'index.html')
    html_ = head(R, title, desc, path, ld, noindex) + '\n' + header(R, active) + body(R) + footer(R)
    write(out, html_)
    if not noindex:
        PAGES.append(path)


# ---------------------------------------------------------------------------
# Inicio
# ---------------------------------------------------------------------------
SLIDES = [
    {'tab': 'Colombia', 'flag': 'co', 'photo': 'bogota', 'title': 'Desde Bogotá, para todo el país',
     'lead': 'Preparamos tu solicitud de visa para Estados Unidos, Reino Unido, Canadá, Australia y Malasia: revisamos tu caso, ordenamos los documentos y te acompañamos hasta la cita.'},
    {'tab': 'Estados Unidos', 'flag': 'us', 'photo': 'capitolio', 'title': 'Visa americana, bien preparada',
     'lead': 'Primera vez, renovación, visas revocadas o perdidas. Revisamos tu perfil antes de diligenciar el DS-160 y te preparamos para la entrevista.'},
    {'tab': 'Más destinos', 'flag': 'gb', 'photo': 'westminster', 'title': 'Reino Unido, Canadá, Australia y Malasia',
     'lead': 'Visas de turismo con solicitud en línea, soportes en orden y cita biométrica cuando el país la exige.'},
]


def home(R):
    imgs, tabs, slides = [], [], []
    for i, s in enumerate(SLIDES):
        act = ' is-active' if i == 0 else ''
        imgs.append(f'<div class="hero__img{act}" data-slide-img>{img(R, s["photo"], eager=i == 0)}</div>')
        tabs.append(f'<button class="hero__tab" type="button" role="tab" id="tab-{i}" aria-controls="slide-{i}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{flag(s["flag"])}{s["tab"]}</button>')
        slides.append(f'''<div class="hero__slide{act}" id="slide-{i}" role="tabpanel" aria-labelledby="tab-{i}"{"" if i == 0 else " aria-hidden=\"true\""}>
              <p class="title">{s["title"]}</p>
              <p class="lead">{s["lead"]}</p>
            </div>''')

    def row(href, code, country, what):
        return f'''<a class="row" href="{R}{href}">{flag(code)}<span class="row__country">{country}</span><span class="row__what">{what}</span><span class="row__go"><span>Ver proceso</span>{ARROW}</span></a>'''

    us_rows = ''.join(row(f'servicios/visa-estados-unidos/{s["slug"]}/', 'us', 'Estados Unidos', s['name']) for s in US_SUBS)
    other_rows = ''.join(row(f'servicios/{c["slug"]}/', c['flag'], c['country'], 'Visa de turismo') for c in COUNTRIES)

    lead_post, rest = POSTS[0], POSTS[1:3]
    post_rows = ''.join(f'''<a class="post-row" href="{R}blog/{p["slug"]}/">
              <div><h3>{p["h1"]}</h3><p>{p["desc"]}</p><p class="post-meta"><span class="tag">{p["category"]}</span></p></div>
              <div class="post-row__img">{img(R, p["image"], sizes="160px", alt=p.get("image_alt"))}</div>
            </a>''' for p in rest)

    chips_dest = ''.join(
        f'<label class="chip"><input type="radio" name="destino" value="{k}"{" checked" if k == "us" else ""}><span>{flag(v["flag"])}{v["country"]}</span></label>'
        for k, v in PLANNER.items())
    first = PLANNER['us']['options'][0]
    docs0 = ''.join(f'<li>{d}</li>' for d in first['docs'])
    chips_proc = ''.join(
        f'<label class="chip"><input type="radio" name="tramite" value="{o["id"]}"{" checked" if j == 0 else ""}><span>{o["label"]}</span></label>'
        for j, o in enumerate(PLANNER['us']['options']))
    planner_json = json.dumps(PLANNER, ensure_ascii=False)

    return f'''
    <section class="hero" aria-roledescription="carrusel" aria-label="Presentación" data-hero>
      <div class="hero__band">
        {"".join(imgs)}
      </div>
      <div class="wrap axis hero__body">
        <div class="axis__side hero__side">
          <div class="hero__tabs" role="tablist" aria-label="Destinos">{"".join(tabs)}</div>
        </div>
        <div class="axis__main">
          {lines(["Asesoría de visas", "en Colombia"])}
          <div class="hero__slides">
            {"".join(slides)}
          </div>
          <div class="actions hero__actions">
            <a class="btn btn--primary" href="#consulta">Solicitar asesoría</a>
            <a class="btn btn--line" href="{wa("Hola, quiero información sobre la visa.")}" target="_blank" rel="noopener" data-track="whatsapp">{icon("wa")}Escribir por WhatsApp</a>
          </div>
        </div>
      </div>
    </section>

    <section class="trust" aria-label="Respaldo">
      <div class="wrap trust__grid" data-reveal>
        <p class="trust__note"><strong>Somos asesores privados, no una entidad oficial.</strong>No somos una embajada ni una oficina del Gobierno. Las tarifas consulares se pagan directamente a cada entidad y la decisión sobre tu visa es siempre del consulado.</p>
        <p class="fact"><span class="fact__value">+2.000</span><span class="fact__label">trámites de visa asesorados</span></p>
        <p class="fact"><span class="fact__value">6 años</span><span class="fact__label">de experiencia en procesos migratorios</span></p>
        <p class="fact"><span class="fact__value">Bogotá</span><span class="fact__label">oficina en la Carrera 45 y atención por WhatsApp</span></p>
      </div>
    </section>

    <section class="section" aria-labelledby="procesos" id="servicios">
      <div class="wrap">
        <div class="svc__head" data-reveal>
          <h2 class="head" id="procesos">Procesos de visa internacional</h2>
          <p class="lead">Elige tu destino y conoce cómo preparamos cada solicitud.</p>
        </div>
        <div class="axis">
          <figure class="axis__side svc__figure shutter" data-shutter>
            {img(R, "salidas", sizes="(max-width: 860px) 70vw, 34vw")}
            <figcaption class="small soft">Tablero de salidas, aeropuerto de Melbourne.</figcaption>
          </figure>
          <div class="axis__main" data-reveal>
            <p class="rows__label">Estados Unidos</p>
            <div class="rows">{us_rows}</div>
            <p class="rows__label rows__group">Turismo</p>
            <div class="rows">{other_rows}</div>
            <p style="margin-top:2rem"><a class="more" href="{R}servicios/">Ver servicios especializados {ARROW}</a></p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--tone" aria-labelledby="guias">
      <div class="wrap">
        <div class="blog-home__head" data-reveal>
          <div><h2 class="head" id="guias">Guías y requisitos</h2><p class="soft">Artículos para preparar tu trámite con información verificada.</p></div>
          <a class="more" href="{R}blog/">Ver todas las guías {ARROW}</a>
        </div>
        <div class="blog-home">
          <a class="post-lead" href="{R}blog/{lead_post["slug"]}/" data-reveal>
            <div class="post-lead__img">{img(R, lead_post["image"], sizes="(max-width: 860px) 100vw, 56vw", alt=lead_post.get("image_alt"))}</div>
            <h3>{lead_post["h1"]}</h3>
            <p>{lead_post["desc"]}</p>
            <p class="post-meta"><span class="tag">{lead_post["category"]}</span><span>Actualizado el {fdate(lead_post["date"])} · {lead_post["read"]} min de lectura</span></p>
          </a>
          <div class="post-list" data-reveal>
            {post_rows}
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="consulta" aria-labelledby="consulta-t">
      <div class="wrap planner">
        <div class="planner__intro" data-reveal>
          <h2 class="head" id="consulta-t">Prepara tu consulta</h2>
          <p class="lead">Elige destino y trámite. Te mostramos qué conviene tener a mano y dejamos listo el mensaje para WhatsApp.</p>
          <p class="small soft">Con tu información a la vista, un asesor te responde con los pasos a seguir y el valor del servicio.</p>
        </div>
        <form class="planner__box section--tone" data-planner onsubmit="return false" aria-label="Arma tu consulta">
          <fieldset><legend>¿A qué país viajas?</legend><div class="chips">{chips_dest}</div></fieldset>
          <fieldset><legend>¿Qué trámite necesitas?</legend><div class="chips" data-tramites>{chips_proc}</div></fieldset>
          <div class="planner__result" aria-live="polite">
            <h3 data-title>Estados Unidos · {first["label"]}</h3>
            <ul class="planner__docs" data-docs>{docs0}</ul>
            <p class="planner__note">Es una lista de referencia. Según tu caso te pediremos más soportes o menos.</p>
            <div class="actions">
              <a class="btn btn--wa" data-wa href="{wa("Hola, quiero asesoría para la visa de Estados Unidos (" + first["label"] + ").")}" target="_blank" rel="noopener" data-track="whatsapp">{icon("wa")}Enviar por WhatsApp</a>
              <a class="btn btn--line" data-more href="{R}{first["url"]}">Ver el proceso</a>
            </div>
          </div>
        </form>
      </div>
      <script type="application/json" id="planner-data">{planner_json}</script>
    </section>

    <section class="section section--tone" aria-labelledby="gerencia">
      <div class="wrap">
        <div class="mgmt__intro" data-reveal>
          <h2 class="head" id="gerencia">Gerencia de visas y procesos migratorios</h2>
          <p class="lead">Somos un equipo de cuatro asesores en Bogotá con credencial de cooperación internacional. Hemos acompañado más de 2.000 trámites y prestado asesoría a jueces de inmigración en cortes de Estados Unidos.</p>
        </div>
        <div class="mosaic">
          <figure class="mosaic__photo shutter" data-shutter>
            {img(R, "sellos", sizes="(max-width: 860px) 100vw, 64vw")}
            <figcaption class="mosaic__note"><strong>Lo que decide el consulado</strong>Preparamos tu solicitud para que sea completa y coherente. La aprobación la decide únicamente el consulado: nadie puede garantizarla.</figcaption>
          </figure>
          <div class="mosaic__side" data-reveal>
            <div class="mosaic__tile">
              <p class="title" style="color:var(--on-navy)">Cooperación internacional</p>
              <p>Colaboramos con la Organización Internacional para las Migraciones y con embajadas mediante nuestra credencial de cooperación.</p>
            </div>
            <dl class="facts">
              <div><dt>Experiencia</dt><dd>6 años</dd></div>
              <div><dt>Trámites asesorados</dt><dd>Más de 2.000</dd></div>
              <div><dt>En la prensa</dt><dd>Revista Semana</dd></div>
              <div><dt>Oficina</dt><dd>{ADDRESS}</dd></div>
            </dl>
          </div>
        </div>
        <p style="margin-top:2.5rem"><a class="more" href="{R}nosotros/">Conoce nuestra historia {ARROW}</a></p>
      </div>
    </section>
{close_band(R)}
'''


ORG_LD = {
    '@context': 'https://schema.org', '@type': 'ProfessionalService', 'name': BRAND, 'url': f'{SITE}/',
    'logo': f'{SITE}/assets/img/logo.png', 'image': f'{SITE}/assets/img/bogota.webp',
    'telephone': PHONE_TEL, 'email': EMAIL, 'areaServed': 'CO',
    'address': {'@type': 'PostalAddress', 'streetAddress': 'Carrera 45', 'addressLocality': 'Bogotá', 'addressCountry': 'CO'},
    'openingHours': 'Mo-Fr 08:00-17:00', 'sameAs': [INSTAGRAM, TIKTOK],
    'description': 'Asesoría privada en visas de Estados Unidos, Reino Unido, Canadá, Australia y Malasia desde Bogotá.',
}


# ---------------------------------------------------------------------------
# Nosotros
# ---------------------------------------------------------------------------
def nosotros(R):
    semana = (f'<p style="margin-top:1.5rem"><a class="more" href="{SEMANA_URL}" target="_blank" rel="noopener">Leer el artículo en Semana {ARROW}</a></p>'
              if SEMANA_URL else '')
    return f'''
    {inner_hero(R, [("nosotros/", "Nosotros")], ["Asesores de visas", "en Bogotá"],
    "Somos una empresa privada de asesoría migratoria con credencial de cooperación internacional. Preparamos solicitudes de visa con información clara y acompañamiento real.",
    side=f"<span>+2.000 trámites asesorados</span><span>6 años de experiencia</span><span>{ADDRESS}</span>",
    actions=f'<a class="btn btn--primary" href="{wa("Hola, quiero hablar con un asesor.")}" target="_blank" rel="noopener" data-track="whatsapp">Hablar con un asesor</a>',
    photo="bogota")}

    <section class="section" aria-labelledby="historia">
      <div class="wrap split">
        <div data-reveal><h2 class="head" id="historia">Nuestra historia</h2><p class="soft">Seis años preparando visas desde Bogotá, casi siempre por recomendación.</p></div>
        <div class="prose" data-reveal>
          <p>Empezamos en Bogotá con una idea sencilla: que pedir una visa no dependiera de la suerte ni de tramitadores sin respaldo. Desde entonces hemos acompañado más de 2.000 trámites, y la mayoría de las personas que nos escriben llegan recomendadas por alguien a quien ya ayudamos.</p>
          <p>Con el tiempo nuestro trabajo pasó de los formularios a la gerencia de procesos migratorios: casos de primera vez, renovaciones, visas revocadas y pasaportes perdidos, y una relación de trabajo con organismos internacionales que nos exige el mismo rigor en cada solicitud.</p>
          <p>Hoy atendemos en nuestra oficina de la Carrera 45 y por WhatsApp a personas de todo el país.</p>
        </div>
      </div>
      <div class="wrap" style="margin-top:clamp(3rem,6vw,5rem)">
        <figure class="photo-pair">
          <div class="shutter" data-shutter>{img(R, "salidas", sizes="(max-width: 760px) 100vw, 58vw")}</div>
          <div class="shutter" data-shutter>{img(R, "sellos", sizes="(max-width: 760px) 100vw, 40vw")}</div>
        </figure>
      </div>
    </section>

    <section class="section section--navy on-navy" aria-labelledby="cooperacion">
      <div class="wrap split">
        <div data-reveal><h2 class="head" id="cooperacion">Cooperación internacional</h2><p class="soft">Nuestro respaldo no está en las promesas sino en con quién trabajamos.</p></div>
        <ul class="milestones" data-reveal>
          <li><strong>Credencial de cooperación internacional</strong><span class="soft">Nos permite colaborar con la Organización Internacional para las Migraciones (OIM) y con embajadas.</span></li>
          <li><strong>Asesoría a jueces de inmigración</strong><span class="soft">Nuestra gerencia ha prestado asesoría a jueces de inmigración en cortes de Estados Unidos.</span></li>
          <li><strong>Encuentros sobre migración</strong><span class="soft">Participamos en espacios sobre migración en América Latina y el Caribe junto a representantes de embajadas.</span></li>
          <li><strong>No somos agencia de viajes</strong><span class="soft">Por eso no tenemos RNT: nuestro trabajo es la asesoría migratoria, no la venta de viajes.</span></li>
        </ul>
      </div>
    </section>

    <section class="section" aria-labelledby="prensa">
      <div class="wrap split">
        <div data-reveal><h2 class="head" id="prensa">En la prensa</h2></div>
        <div data-reveal>
          <p class="quote">La revista Semana publicó un artículo sobre nuestra labor de asesoría migratoria en Nueva York.</p>
          {semana}
        </div>
      </div>
    </section>

    <section class="section section--tone" aria-labelledby="equipo">
      <div class="wrap split">
        <div data-reveal><h2 class="head" id="equipo">Un equipo de cuatro asesores</h2></div>
        <div class="prose" data-reveal>
          <p>Por seguridad, y siguiendo las recomendaciones de las embajadas, no publicamos fotografías del equipo. Te atendemos con nombre propio por WhatsApp y en la oficina.</p>
          <ul>
            <li>Te decimos con claridad qué puede hacer una asesoría y qué decide el consulado.</li>
            <li>Revisamos cada documento antes de que lo presentes.</li>
            <li>Respondemos por WhatsApp en cada etapa del trámite.</li>
          </ul>
        </div>
      </div>
    </section>
{close_band(R)}
'''


# ---------------------------------------------------------------------------
# Servicios
# ---------------------------------------------------------------------------
def servicios(R):
    us_list = ''.join(f'<span>{s["name"]}</span>' for s in US_SUBS)
    tiles = [f'''<a class="dest dest--us" href="{R}servicios/visa-estados-unidos/">
            {img(R, "capitolio", eager=True, sizes="(max-width: 860px) 100vw, 66vw")}
            <div class="dest__body">{flag("us")}<h2>Estados Unidos</h2><div class="dest__us-list">{us_list}</div></div>
          </a>''']
    for c in COUNTRIES:
        tiles.append(f'''<a class="dest dest--{c["cls"]}" href="{R}servicios/{c["slug"]}/">
            {img(R, c["photo"], sizes="(max-width: 860px) 50vw, 33vw")}
            <div class="dest__body">{flag(c["flag"])}<h2>{c["country"]}</h2><p>Visa de turismo</p></div>
          </a>''')
    return f'''
    {inner_hero(R, [("servicios/", "Servicios")], ["Servicios", "especializados"],
    "En visas para Estados Unidos, Reino Unido, Canadá, Australia y Malasia, desde Bogotá. Cada destino tiene su página con lo que necesitas saber antes de empezar.",
    side="<span>Procesos de visa internacional</span>", photo="salidas")}
    <section aria-label="Destinos">
      <div class="wrap">
        <div class="dest-grid" data-reveal>
          {"".join(tiles)}
        </div>
      </div>
    </section>
{docs_section(R)}
    <section class="section section--tone" aria-labelledby="pago">
      <div class="wrap cta-band" data-reveal>
        <div><h2 class="head" id="pago">Pago seguro con ePayco</h2><p class="soft">Pagas la asesoría en línea, con los medios que ofrece ePayco. Las tarifas consulares no las cobramos nosotros: se pagan directamente a cada entidad.</p></div>
        <div class="actions">
          <a class="btn btn--primary" href="{wa("Hola, no sé qué visa necesito. ¿Me ayudan?")}" target="_blank" rel="noopener" data-track="whatsapp">¿No sabes qué visa necesitas?</a>
        </div>
      </div>
    </section>
{close_band(R)}
'''


def service_detail(R, s, country, flag_code, photo, trail, pay_id):
    msg = f'Hola, quiero asesoría para: {s["title"]}.'
    toc = [('acompanamiento', 'Cómo te acompañamos'), ('documentos', 'Documentos que suelen pedir'), ('tiempos', 'Tiempos y pagos'), ('ten-en-cuenta', 'Ten en cuenta')]
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    help_ = ''.join(f'<li>{x}</li>' for x in s['help'])
    docs = ''.join(f'<li>{x}</li>' for x in s['docs'])
    related = [p for p in POSTS if country in p.get('countries', '')]
    related = (related + [p for p in POSTS if p not in related])[:3]
    rel = ''.join(post_card(R, p) for p in related)
    return f'''
    {inner_hero(R, trail, s["h1"], s["lead"],
    side=f'{flag(flag_code)}<span>{country}</span><span>Visa de {"turismo" if flag_code != "us" else "turismo B1/B2"}</span>',
    actions=f'''<a class="btn btn--primary" href="{wa(msg)}" target="_blank" rel="noopener" data-track="whatsapp">Solicitar asesoría</a>
              <a class="btn btn--line" href="{R}contacto/" data-pay="{pay_id}">{icon("card")}Pagar con ePayco</a>''',
    photo=photo)}

    <section class="section">
      <div class="wrap doc-layout">
        <aside class="doc-aside">
          <nav class="toc" aria-label="En esta página"><h2>En esta página</h2><ol>{toc_html}</ol></nav>
          <div class="aside-card">
            <h2>¿Empezamos?</h2>
            <p>Escríbenos con tu caso y te respondemos con los pasos y el valor del servicio.</p>
            <div class="actions"><a class="btn btn--wa" href="{wa(msg)}" target="_blank" rel="noopener" data-track="whatsapp">{icon("wa")}WhatsApp</a></div>
          </div>
        </aside>
        <div class="prose" data-reveal>
          <h2 id="acompanamiento">Cómo te acompañamos</h2>
          <ul>{help_}</ul>
          <h2 id="documentos">Documentos que suelen pedir</h2>
          <p>Es una lista de referencia; según tu caso te pediremos más o menos soportes.</p>
          <ul>{docs}</ul>
          <h2 id="tiempos">Tiempos y pagos</h2>
          <p>{s["times"]}</p>
          <div class="inline-cta"><p>¿Quieres que revisemos tus documentos?</p><a class="btn btn--primary" href="{wa("Hola, quiero que revisen mis documentos para: " + s["title"] + ".")}" target="_blank" rel="noopener">Escribir al asesor</a></div>
          <h2 id="ten-en-cuenta">Ten en cuenta</h2>
          <p>{s["note"]}</p>
          <p>Somos una empresa privada de asesoría: no representamos a ningún gobierno ni a sus consulados.</p>
        </div>
      </div>
    </section>

    <section class="section section--tone" aria-labelledby="guias-rel">
      <div class="wrap">
        <div class="blog-home__head" data-reveal><h2 class="head" id="guias-rel">Guías relacionadas</h2><a class="more" href="{R}blog/">Ver el blog {ARROW}</a></div>
        <div class="post-grid" data-reveal>{rel}</div>
      </div>
    </section>
{docs_section(R)}
{close_band(R)}
'''


def service_ld(name, desc, path):
    return {'@context': 'https://schema.org', '@type': 'Service', 'name': name, 'description': desc, 'serviceType': 'Asesoría de visas',
            'areaServed': 'CO', 'provider': {'@type': 'ProfessionalService', 'name': BRAND, 'url': f'{SITE}/'}, 'url': f'{SITE}/{path}'}


def us_hub(R):
    procs = ''.join(f'''<a class="row row--proc" href="{R}servicios/visa-estados-unidos/{s["slug"]}/">
            <span class="row__country">{s["name"]}</span><span class="row__what">{s["short"]}</span><span class="row__go"><span>Ver el proceso</span>{ARROW}</span>
          </a>''' for s in US_SUBS)
    related = [p for p in POSTS if 'Estados Unidos' in p.get('countries', '')][:3]
    rel = ''.join(post_card(R, p) for p in related)
    return f'''
    {inner_hero(R, [("servicios/", "Servicios"), ("servicios/visa-estados-unidos/", "Estados Unidos")], ["Visa americana", "desde Bogotá"],
    "Te acompañamos en los cuatro casos más comunes: la primera solicitud, la renovación, la visa revocada y la visa perdida o robada.",
    side=f'{flag("us")}<span>Estados Unidos</span><span>Visa de turismo B1/B2</span>',
    actions=f'''<a class="btn btn--primary" href="{wa("Hola, quiero asesoría para la visa americana.")}" target="_blank" rel="noopener" data-track="whatsapp">Solicitar asesoría</a>
              <a class="btn btn--line" href="{R}contacto/" data-pay="visa-estados-unidos">{icon("card")}Pagar con ePayco</a>''',
    photo="capitolio")}

    <section class="section" aria-labelledby="casos">
      <div class="wrap">
        <div class="svc__head" data-reveal><h2 class="head" id="casos">¿Cuál es tu caso?</h2><p class="lead">Cada situación tiene requisitos y riesgos distintos. Elige la tuya.</p></div>
        <div class="axis"><figure class="axis__side svc__figure shutter" data-shutter>{img(R, "sellos", sizes="(max-width: 860px) 70vw, 34vw")}<figcaption class="small soft">Sellos migratorios en un pasaporte.</figcaption></figure><div class="axis__main rows" data-reveal>{procs}</div></div>
      </div>
    </section>

    <section class="section section--tone" aria-labelledby="guias-rel">
      <div class="wrap">
        <div class="blog-home__head" data-reveal><h2 class="head" id="guias-rel">Guías sobre la visa americana</h2><a class="more" href="{R}blog/">Ver el blog {ARROW}</a></div>
        <div class="post-grid" data-reveal>{rel}</div>
      </div>
    </section>
{docs_section(R)}
{close_band(R)}
'''


# ---------------------------------------------------------------------------
# Blog
# ---------------------------------------------------------------------------
def blog_index(R):
    lead = POSTS[0]
    buttons = '<button type="button" aria-pressed="true" data-filter="">Todas</button>' + ''.join(
        f'<button type="button" aria-pressed="false" data-filter="{esc(c)}">{c}</button>' for c in CATEGORIES)
    cards = ''.join(post_card(R, p) for p in POSTS)
    return f'''
    {inner_hero(R, [("blog/", "Blog")], ["Guías de visas", "para colombianos"],
    "Requisitos, tiempos y pasos del trámite, explicados con claridad y actualizados cuando cambian las reglas.",
    side="<span>Escritas por nuestra gerencia de visas</span>", photo="sellos")}

    <section class="section" aria-labelledby="destacado">
      <div class="wrap blog-home">
        <a class="post-lead" href="{R}blog/{lead["slug"]}/" data-reveal>
          <div class="post-lead__img">{img(R, lead["image"], eager=True, sizes="(max-width: 860px) 100vw, 56vw", alt=lead.get("image_alt"))}</div>
        </a>
        <div data-reveal style="align-self:end">
          <h2 class="head" id="destacado" style="font-size:clamp(1.75rem,1.2rem + 1.6vw,2.75rem)">{lead["h1"]}</h2>
          <p style="margin-top:1rem">{lead["desc"]}</p>
          <p class="post-meta"><span class="tag">{lead["category"]}</span><span>Actualizado el {fdate(lead["date"])} · {lead["read"]} min de lectura</span></p>
          <div class="actions" style="margin-top:1.75rem"><a class="btn btn--primary" href="{R}blog/{lead["slug"]}/">Leer la guía</a></div>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="articulos">
      <div class="wrap">
        <div data-reveal><h2 class="head" id="articulos">Todos los artículos</h2><div class="filters" role="group" aria-label="Filtrar por categoría">{buttons}</div></div>
        <div class="post-grid" style="margin-top:clamp(2.5rem,4vw,3.5rem)" data-posts data-reveal>{cards}</div>
      </div>
    </section>
{close_band(R, "¿Leíste la guía y quieres que revisemos tu caso? Escríbenos.")}
'''


def article(R, p):
    toc = ''.join(f'<li><a href="#{i}">{re.sub("<.*?>", "", t)}</a></li>' for i, t in p['toc'])
    related = [q for q in POSTS if q['slug'] != p['slug']][:3]
    rel = ''.join(post_card(R, q) for q in related)
    svc = p.get('service', 'servicios/')
    return f'''
    <article>
    {inner_hero(R, [("blog/", "Blog"), (f"blog/{p['slug']}/", p["h1"])], None,
    f'<span class="byline">Por <strong>Gerencia de visas, {BRAND}</strong> · Actualizado el {fdate(p["date"])}</span>',
    side=f'<span class="tag">{p["category"]}</span><span>{p["read"]} min de lectura</span>', h1=p["h1"], photo=p["image"], photo_alt=p.get("image_alt"))}
      <section class="section">
        <div class="wrap doc-layout">
          <aside class="doc-aside">
            <nav class="toc" aria-label="En este artículo"><h2>En este artículo</h2><ol>{toc}</ol></nav>
            <div class="aside-card">
              <h2>¿Quieres que revisemos tu caso?</h2>
              <p>Te respondemos por WhatsApp con los pasos y el valor del servicio.</p>
              <div class="actions"><a class="btn btn--primary" href="{R}{svc}">Ver el servicio</a></div>
            </div>
          </aside>
          <div class="prose" data-reveal>
            <div class="summary"><strong>Resumen</strong>{p["summary"]}</div>
            {p["body"].replace("{R}", R).replace("{WA}", wa("Hola, leí la guía " + p["title"] + " y quiero asesoría."))}
          </div>
        </div>
      </section>
    </article>
    <section class="section section--tone" aria-labelledby="relacionados">
      <div class="wrap">
        <div class="blog-home__head"><h2 class="head" id="relacionados">Artículos relacionados</h2><a class="more" href="{R}blog/">Ver el blog {ARROW}</a></div>
        <div class="post-grid" data-reveal>{rel}</div>
      </div>
    </section>
{close_band(R)}
'''


# ---------------------------------------------------------------------------
# Contacto
# ---------------------------------------------------------------------------
def contacto(R):
    q = quote(MAP_QUERY)
    return f'''
    {inner_hero(R, [("contacto/", "Contacto")], ["Contacto y oficina", "en Bogotá"],
    "Elige el canal que prefieras. Te respondemos en horario de atención.",
    side=f"<span>{HOURS}</span>", photo="candelaria")}

    <section class="section section--tone" aria-labelledby="canales">
      <div class="wrap axis">
        <div class="axis__side"><h2 class="head" id="canales">Canales de atención</h2></div>
        <div class="axis__main channels" data-reveal>
          <div class="channel"><h3>WhatsApp</h3><p>{PHONE} · el canal más rápido para empezar tu trámite.</p><a class="btn btn--wa" href="{wa("Hola, quiero información sobre un trámite de visa.")}" target="_blank" rel="noopener" data-track="whatsapp">{icon("wa")}Escribir ahora</a></div>
          <div class="channel"><h3>Teléfono</h3><p>{PHONE} · {HOURS.lower()}</p><a class="btn btn--line" href="tel:{PHONE_TEL}">Llamar</a></div>
          <div class="channel"><h3>Correo</h3><p>{EMAIL} · para enviar documentos o radicar una PQRS.</p><a class="btn btn--line" href="mailto:{EMAIL}">Enviar correo</a></div>
        </div>
      </div>
    </section>

    <section class="section" id="ubicacion" aria-labelledby="llegar">
      <div class="wrap split">
        <div data-reveal>
          <h2 class="head" id="llegar">Cómo llegar a la oficina</h2>
          <dl class="nap" style="margin-top:2rem">
            <div><dt>Razón social</dt><dd>{BRAND}</dd></div>
            <div><dt>Dirección</dt><dd>{ADDRESS}</dd></div>
            <div><dt>Horario</dt><dd>{HOURS}</dd></div>
            <div><dt>Teléfono y WhatsApp</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd></div>
            <div><dt>Correo</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
            <div><dt>Síguenos</dt><dd><div class="socials"><a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">{icon("ig")}</a><a href="{TIKTOK}" target="_blank" rel="noopener" aria-label="TikTok">{icon("tt")}</a></div></dd></div>
          </dl>
        </div>
        <div data-reveal>
          <div class="map"><iframe title="Mapa de la oficina en {esc(ADDRESS)}" src="https://maps.google.com/maps?q={q}&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
          <p style="margin-top:1rem"><a class="more" href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener">Abrir en Google Maps {ARROW}</a></p>
        </div>
      </div>
    </section>
    <section class="section section--tone" aria-labelledby="ciudad">
      <div class="wrap">
        <div class="blog-home__head" data-reveal><h2 class="head" id="ciudad">Te atendemos en Bogotá</h2><p class="soft" style="max-width:44ch">Presencialmente en la oficina o por WhatsApp desde cualquier ciudad de Colombia.</p></div>
        <figure class="photo-pair">
          <div class="shutter" data-shutter>{img(R, "bogota", sizes="(max-width: 760px) 100vw, 58vw")}</div>
          <div class="shutter" data-shutter>{img(R, "taxi", sizes="(max-width: 760px) 100vw, 40vw")}</div>
        </figure>
      </div>
    </section>
{close_band(R, "Cuéntanos por WhatsApp tu nombre y el país al que viajas.")}
'''


# ---------------------------------------------------------------------------
# Legales
# ---------------------------------------------------------------------------
NOTICE = '<blockquote>Este documento es una versión preliminar y se reemplazará por el texto definitivo aprobado por la empresa.</blockquote>'

LEGAL_BODY = {
    'politica-de-tratamiento-de-datos': f'''
      <h2>Responsable del tratamiento</h2>
      <p>{BRAND}, con domicilio en {ADDRESS}, es responsable del tratamiento de los datos personales que recoge a través de este sitio, de WhatsApp, del correo electrónico y de la atención en oficina. Contacto: {EMAIL}.</p>
      <h2>Qué datos recogemos</h2>
      <ul><li>Datos de identificación y contacto: nombre, documento, teléfono y correo.</li><li>Datos del trámite: pasaporte, historial de viajes, información laboral, financiera y familiar que se necesita para la solicitud de visa.</li><li>Datos de navegación del sitio, de forma agregada.</li></ul>
      <h2>Para qué los usamos</h2>
      <ul><li>Prestar el servicio de asesoría y diligenciar las solicitudes que nos autorices.</li><li>Comunicarnos contigo sobre el estado de tu trámite.</li><li>Cumplir obligaciones legales, contables y tributarias.</li></ul>
      <p>No vendemos ni cedemos tus datos. Solo los compartimos con las entidades ante las que presentas tu solicitud y con proveedores necesarios para prestar el servicio, bajo acuerdos de confidencialidad.</p>
      <h2>Tus derechos</h2>
      <p>Según la Ley 1581 de 2012 puedes conocer, actualizar, rectificar y suprimir tus datos, revocar la autorización y presentar quejas ante la Superintendencia de Industria y Comercio. Para ejercerlos escribe a {EMAIL}.</p>
      <h2>Datos sensibles</h2>
      <p>Algunos trámites requieren información sensible. No estás obligado a entregarla; si decides hacerlo, la usaremos únicamente para tu solicitud.</p>''',
    'politica-de-manejo-de-casos': '''
      <h2>Qué hacemos</h2>
      <p>Revisamos tu caso, te indicamos los requisitos vigentes, organizamos y revisamos tus documentos, diligenciamos los formularios con la información que nos entregas, programamos las citas y te preparamos para la entrevista cuando aplica.</p>
      <h2>Qué decides tú</h2>
      <p>Tú apruebas la información que se presenta en tu nombre y eres responsable de que sea verdadera. Nunca diligenciaremos datos falsos ni documentos alterados.</p>
      <h2>Qué decide el consulado</h2>
      <p>La aprobación o negación de una visa es una decisión exclusiva de la autoridad de cada país. Ninguna asesoría puede garantizar el resultado.</p>
      <h2>Confidencialidad</h2>
      <p>Cada caso lo atiende un asesor asignado. Tus documentos se usan solo para tu trámite y se manejan según nuestra política de tratamiento de datos.</p>''',
    'terminos-y-condiciones': f'''
      <h2>El servicio</h2>
      <p>{BRAND} presta servicios privados de asesoría en solicitudes de visa. No es una entidad oficial ni representa a ningún gobierno o consulado.</p>
      <h2>Honorarios y tarifas oficiales</h2>
      <p>El valor de la asesoría se informa antes de empezar y se paga a través de ePayco o de los medios que indiquemos. Las tarifas consulares, de visa o de biometría se pagan directamente a cada entidad y no están incluidas en nuestros honorarios.</p>
      <h2>Responsabilidades</h2>
      <p>Nos comprometemos a prestar el servicio con diligencia. El cliente se compromete a entregar información veraz y completa y a asistir a las citas programadas.</p>
      <h2>Uso del sitio</h2>
      <p>La información de este sitio es orientativa y puede cambiar cuando las autoridades actualizan sus requisitos. Siempre la validamos al iniciar cada caso.</p>''',
    'politica-de-reembolsos': '''
      <h2>Cuándo hay reembolso</h2>
      <ul><li>Si cancelas antes de que empecemos a trabajar en tu caso, devolvemos el valor pagado menos los costos de la transacción.</li><li>Si no podemos prestar el servicio por una causa atribuible a nosotros.</li></ul>
      <h2>Cuándo no hay reembolso</h2>
      <ul><li>Cuando la visa es negada: la decisión es del consulado y el servicio de asesoría ya se prestó.</li><li>Sobre las tarifas consulares, que se pagan directamente a cada entidad.</li></ul>
      <h2>Cómo pedirlo</h2>
      <p>Escríbenos por correo o radica una PQRS indicando tu nombre, el trámite y el comprobante de pago. Respondemos en un máximo de 15 días hábiles.</p>''',
    'pqrs': f'''
      <h2>Qué puedes radicar</h2>
      <p>Peticiones, quejas, reclamos y sugerencias sobre nuestro servicio, el tratamiento de tus datos o un pago.</p>
      <h2>Cómo radicarla</h2>
      <ul><li>Por correo a <a href="mailto:{EMAIL}">{EMAIL}</a>, con el asunto «PQRS».</li><li>Por WhatsApp al {PHONE}.</li><li>En la oficina: {ADDRESS}, {HOURS.lower()}.</li></ul>
      <p>Incluye tu nombre, documento, datos de contacto, el trámite al que se refiere y una descripción de la solicitud.</p>
      <h2>Plazo de respuesta</h2>
      <p>Te confirmamos la recepción el mismo día hábil y respondemos de fondo en un máximo de 15 días hábiles.</p>''',
}


def legal_page(slug, name, sub):
    def body(R):
        return f'''
    {inner_hero(R, [(f"{slug}/", name)], None, sub, h1=name, photo="sellos")}
    <section class="section section--tone" style="padding-top:clamp(3rem,5vw,4.5rem)">
      <div class="wrap axis">
        <div class="axis__side"><p class="small soft">Última actualización: {fdate(date.today().isoformat())}</p></div>
        <div class="axis__main prose" data-reveal>{NOTICE}{LEGAL_BODY[slug]}</div>
      </div>
    </section>
{docs_section(R, "Otros documentos", "Todas nuestras políticas, en un solo lugar.")}
'''
    return body


def creditos(R):
    data = json.load(open(os.path.join(ROOT, 'assets', 'credits.json'), encoding='utf-8'))
    rows = []
    for c in data:
        key = next(v for k, v in CREDIT_KEYS.items() if k in c['file'])
        name = re.sub(r'\s*\(\d+\)$', '', c['title'])
        rows.append(f'''<li class="credit">{img(R, key, sizes="160px", eager=True)}<div><strong>{esc(name)}</strong>
              <span>{esc(c["creator"])} · <a href="{c["licenseUrl"]}" target="_blank" rel="noopener">{c["license"]}</a> · <a href="{c["page"]}" target="_blank" rel="noopener">Ver la fuente</a></span></div></li>''')
    return f'''
    {inner_hero(R, [("creditos/", "Créditos")], None, "Las fotografías de este sitio vienen de colecciones abiertas y se usan según su licencia. Muestran los destinos y la ciudad; no son fotos de nuestra oficina ni de nuestros clientes.", h1="Créditos de fotografías", photo="salidas")}
    <section class="section section--tone">
      <div class="wrap"><ul class="credits" data-reveal>{"".join(rows)}</ul></div>
    </section>
'''


def not_found(R):
    return f'''
    <section class="section nf">
      <div class="wrap axis">
        <div class="axis__main">
          {lines(["Esta página", "no existe"])}
          <p class="lead" style="margin-top:1.5rem">Puede que el enlace haya cambiado. Vuelve al inicio o escríbenos por WhatsApp.</p>
          <div class="actions" style="margin-top:2rem"><a class="btn btn--primary" href="{R or './'}">Ir al inicio</a><a class="btn btn--line" href="{R}servicios/">Ver servicios</a></div>
        </div>
      </div>
    </section>'''


# ---------------------------------------------------------------------------
# Construcción
# ---------------------------------------------------------------------------
def build():
    page('', 'Asesoría de visas en Bogotá, Colombia', 'Asesoría privada de visas en Bogotá para Estados Unidos, Reino Unido, Canadá, Australia y Malasia. Revisión de documentos, citas y atención por WhatsApp.', home, '', [ORG_LD])
    page('nosotros/', 'Quiénes somos: asesores de visas en Bogotá', 'Empresa privada de asesoría migratoria en Bogotá con credencial de cooperación internacional, 6 años de experiencia y más de 2.000 trámites.', nosotros, 'nosotros/', [breadcrumb_ld([('nosotros/', 'Nosotros')])])
    page('servicios/', 'Servicios especializados en visas', 'Procesos de visa internacional desde Bogotá: Estados Unidos (primera vez, renovación, revocada, perdida), Reino Unido, Canadá, Australia y Malasia.', servicios, 'servicios/', [breadcrumb_ld([('servicios/', 'Servicios')])])
    p_us = 'servicios/visa-estados-unidos/'
    page(p_us, US['title'], US['desc'], us_hub, 'servicios/', [service_ld('Asesoría para visa americana', US['desc'], p_us), breadcrumb_ld([('servicios/', 'Servicios'), (p_us, 'Estados Unidos')])])
    for s in US_SUBS:
        path = f'{p_us}{s["slug"]}/'
        trail = [('servicios/', 'Servicios'), (p_us, 'Estados Unidos'), (path, s['name'])]
        page(path, s['title'], s['desc'], lambda R, s=s, trail=trail: service_detail(R, s, 'Estados Unidos', 'us', 'capitolio', trail, f'us-{s["slug"]}'),
             'servicios/', [service_ld(s['title'], s['desc'], path), breadcrumb_ld(trail)])
    for c in COUNTRIES:
        path = f'servicios/{c["slug"]}/'
        trail = [('servicios/', 'Servicios'), (path, c['country'])]
        page(path, c['title'], c['desc'], lambda R, c=c, trail=trail: service_detail(R, c, c['country'], c['flag'], c['photo'], trail, c['slug']),
             'servicios/', [service_ld(c['title'], c['desc'], path), breadcrumb_ld(trail)])
    page('blog/', 'Blog: guías de visas para colombianos', 'Guías actualizadas sobre requisitos de visa, citas y trámites para colombianos, escritas por nuestra gerencia de visas en Bogotá.', blog_index, 'blog/', [breadcrumb_ld([('blog/', 'Blog')])])
    for p in POSTS:
        path = f'blog/{p["slug"]}/'
        ld = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': p['title'], 'description': p['desc'],
              'datePublished': p.get('published', p['date']), 'dateModified': p['date'], 'image': f'{SITE}/assets/img/{p["image"]}.webp',
              'author': {'@type': 'Organization', 'name': BRAND}, 'publisher': {'@type': 'Organization', 'name': BRAND, 'logo': {'@type': 'ImageObject', 'url': f'{SITE}/assets/img/logo.png'}},
              'mainEntityOfPage': f'{SITE}/{path}'}
        page(path, p['title'], p['desc'], lambda R, p=p: article(R, p), 'blog/', [ld, breadcrumb_ld([('blog/', 'Blog'), (path, p['title'])])])
    page('contacto/', 'Contacto y oficina en Bogotá', f'Escríbenos por WhatsApp, llámanos o visítanos en {ADDRESS}. Asesoría de visas de lunes a viernes.', contacto, 'contacto/',
         [dict(ORG_LD, **{'@type': 'ProfessionalService'}), breadcrumb_ld([('contacto/', 'Contacto')])])
    for slug, name, sub in LEGAL:
        page(f'{slug}/', name, sub, legal_page(slug, name, sub), '', [breadcrumb_ld([(f'{slug}/', name)])])
    page('creditos/', 'Créditos de fotografías', 'Fuentes y licencias de las fotografías usadas en el sitio.', creditos, '', [breadcrumb_ld([('creditos/', 'Créditos')])])
    # 404 en la raíz con rutas absolutas al sitio publicado
    page('', 'Página no encontrada', 'La página que buscas no existe.', not_found, '', noindex=True, file='404.html', base=SITE + '/')

    urls = '\n'.join(f'  <url><loc>{SITE}/{p}</loc><lastmod>{date.today().isoformat()}</lastmod></url>' for p in PAGES)
    write('sitemap.xml', f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    write('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /legacy/\n\nSitemap: {SITE}/sitemap.xml\n')
    print(f'{len(PAGES) + 1} páginas generadas')


if __name__ == '__main__':
    build()
