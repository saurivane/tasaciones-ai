# Plan de SEO San Isidro Gestión

## 1. Metaetiquetas y Open Graph
Añadir las siguientes etiquetas en el `<head>` de `index.html`:

```html
<!-- SEO Principal -->
<meta name="description" content="Valoración inmobiliaria gratuita y profesional en Madrid con San Isidro Gestión. Tasación inmediata con IA.">
<meta name="keywords" content="tasación pisos madrid, valoración inmuebles, tasador online gratis, san isidro gestión, inmobiliaria carabanchel">
<meta name="author" content="San Isidro Gestión">
<meta name="robots" content="index, follow">

<!-- Redes Sociales (Open Graph) -->
<meta property="og:title" content="Valoración Inmobiliaria IA - San Isidro Gestión">
<meta property="og:description" content="¿Sabes cuánto vale tu casa? Obtén una valoración profesional gratuita en segundos.">
<meta property="og:image" content="https://sanisidrogestion.es/static/logo.png">
<meta property="og:url" content="https://sanisidrogestion.es/">
<meta property="og:type" content="website">

<!-- Canonical (Evitar contenido duplicado) -->
<link rel="canonical" href="https://sanisidrogestion.es/">
```

## 2. Datos Estructurados (JSON-LD)
Añadir este script dentro del `<body>` o `<head>` para definir el negocio local:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "San Isidro Gestión",
  "image": "https://sanisidrogestion.es/static/logo.png",
  "@id": "https://sanisidrogestion.es",
  "url": "https://sanisidrogestion.es",
  "telephone": "910242213",
  "email": "sanisidrogestionsl@gmail.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "C/ Antonio López, 47 Local",
    "addressLocality": "Madrid",
    "postalCode": "28019",
    "addressCountry": "ES"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 40.3957, 
    "longitude": -3.7089 
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:30",
      "closes": "14:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "17:00",
      "closes": "20:30"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "10:00",
      "closes": "14:00"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/tu-pagina",
    "https://www.instagram.com/tu-usuario"
  ]
}
</script>
```

## 3. Archivos Técnicos
Crear estos archivos en la carpeta `app/static/`:

**robots.txt**
```text
User-agent: *
Allow: /
Sitemap: https://sanisidrogestion.es/sitemap.xml
```

**sitemap.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://sanisidrogestion.es/</loc>
    <lastmod>2026-02-07</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

## 4. Mejoras Semánticas
*   Asegurar que todas las imágenes `<img>` tengan el atributo `alt` descriptivo.
*   Verificar que solo haya un `<h1>` en la página (ya correcto: "¿Quanto vale tu casa?").
