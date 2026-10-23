# Visas y Pasaportes Colombia · Sitio web

Sitio estático (HTML, CSS y JS sin dependencias), igual que DriveGo. Se publica en cualquier hosting estático; el flujo de `.github/workflows/pages.yml` lo despliega en GitHub Pages con cada push.

## Vista previa

```bash
python3 -m http.server 8080
# abrir http://localhost:8080
```

Para activar GitHub Pages: Settings > Pages > Source: **GitHub Actions**. El sitio queda en https://jhonbermudezz.github.io/visas/.

## Cómo se edita

Todo el sitio sale de `tools/build.py` (cabecera, menú, pie, páginas y textos de servicios) y de los artículos en `content/blog/`. Después de cualquier cambio:

```bash
python3 tools/build.py
```

### Publicar un artículo en el blog

1. Copiar un archivo de `content/blog/` con un nombre nuevo, por ejemplo `cita-cas-bogota.html` (el nombre del archivo será la URL: `/blog/cita-cas-bogota/`).
2. Cambiar el encabezado: `h1` (título corto en la página), `title` (título para Google), `desc`, `category`, `date`, `read` (minutos), `image` (clave de una foto en `PHOTOS`), `countries`, `service` y `summary`.
3. Escribir el cuerpo en HTML. Cada `<h2 id="...">` aparece solo en el índice del artículo. `{WA}` se reemplaza por el enlace de WhatsApp.
4. Ejecutar `python3 tools/build.py`. El artículo aparece en el blog, en el inicio (si es el más reciente o tiene `featured: si`), en las páginas de servicio relacionadas y en el sitemap.

Si el cliente necesita publicar sin tocar archivos, el siguiente paso es conectar un panel (Decap CMS sobre este mismo repositorio, o migrar el blog a WordPress).

## Estructura (según wireframes y la reunión del 16 de octubre)

- **Inicio:** menú con desplegable de servicios con banderas, carrusel principal (Colombia, Estados Unidos, más destinos), franja de respaldo y aviso de independencia, procesos de visa internacional, blog como tercera sección, armador de consulta por WhatsApp, gerencia de visas y procesos migratorios y cierre de contacto.
- **Servicios:** página "Servicios especializados" con mosaico de destinos, documentos y políticas en lugar de tablas comparativas, y pago con ePayco.
  - Estados Unidos: primera vez, renovación, visa revocada, visa perdida o robada.
  - Reino Unido, Canadá, Australia y Malasia: turismo.
- **Nosotros:** historia, cooperación internacional (OIM, embajadas, jueces de inmigración), prensa (Semana) y equipo sin fotografías.
- **Blog:** filtros por categoría, artículo destacado, índice en cada artículo y artículos relacionados.
- **Contacto:** canales, datos de la oficina y mapa. Sin formulario.
- **Legales:** tratamiento de datos, manejo de casos, términos, reembolsos, PQRS y créditos de fotografías.
- Botones flotantes de WhatsApp (y llamada en móvil). Sin preguntas frecuentes ni formularios.

## Diseño

- Colores tomados del logo: azul rey `#1438A6` y rojo `#C81E2B`, sobre un azul marino institucional `#0C1F4D` y un fondo gris muy claro `#F5F6F8`.
- Tipografía: Geist en todo el sitio, con títulos grandes y apretados.
- Cabeceras a pantalla completa con foto y velo azul marino, botones tipo píldora y esquinas suaves en fotos y bloques.
- Movimiento: carrusel con barras de progreso, fotos de cabecera que se desplazan más lento que la página, cifras que cuentan al aparecer y entradas escalonadas.

### Versión anterior

La primera versión (clásica, con serifa) quedó guardada como copia fija en `legacy/`, visible en https://jhonbermudezz.github.io/visas/legacy/ y fuera de los buscadores. No se regenera con el script.
- Fotografías de destinos y de Bogotá de colecciones abiertas (Wikimedia Commons y Openverse); créditos en `/creditos/` y en `assets/credits.json`.
- Imágenes ilustrativas de viajeros, documentos y el mapa del mundo generadas con IA en KIE (modelo nano-banana): `hero-familia`, `hero-eeuu`, `hero-destinos`, `documentos`, `entrega` y `mapa` en `assets/img/`. No muestran clientes reales ni al equipo; reemplazarlas por fotos propias cuando el cliente las envíe.

## Pendiente antes de publicar

En `tools/build.py` (bloque "Datos del negocio"):

- Teléfono y WhatsApp, correo, dirección exacta, horario y dominio definitivo (`SITE`).
- Enlaces de Instagram y TikTok.
- Enlace del artículo de Semana (`SEMANA_URL`); al llenarlo aparece el botón "Leer el artículo".

En `assets/js/main.js`:

- `WHATSAPP` (mismo número) y `EPAYCO_LINKS`: un enlace de pago por servicio. Mientras estén vacíos, "Pagar con ePayco" abre WhatsApp pidiendo el enlace.

Contenido del cliente:

- Textos de los slides 2 y 3, tabla de precios, artículos del blog (los actuales son borradores para validar), videos corporativos, fotos del negocio y documentos legales definitivos (los actuales son borradores).
- Logo en alta resolución o vectorial (el actual se recortó de la imagen enviada).
