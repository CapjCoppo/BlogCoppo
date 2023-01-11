AUTHOR = 'Corporación Administrativa Poder Judicial'
SITENAME = 'Blog jurisdiccional Copiapó'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DATE_FORMATS = {"es": "%d-%m-%Y"}

# Blogroll
LINKS = (('Portal Firmas', 'https://funpfirmagob.pjud.cl/PFIRMAFUNWEB/jsp/Login/Login.jsp'),
         ('Portal Personas', 'https://personas.pjud.cl/portalpersonassrh/servlet/com.portalpersonas.login'),
         ('Mesa de Ayuda', 'http://mesaayuda.intranet.pjud/mesa_ayuda/index.php'),)

# Social widget
"""SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)"""

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Linea en donde aloja el sitio para github saque la página
OUTPUT_PATH = 'docs/'

#Linea de donde obtiene el template base de la página
THEME = 'themes/pelican-alchemy/alchemy'