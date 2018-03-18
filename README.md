crossrefs
=========

Just a generator of documents of lists of (item, definition) where
each item that appears on a definition is linked to the item itself.

F.e., the following input:

    [Zeus]
    
    Lived in Mount Olympus. Married to Hera.
    
    [Hera]
    
    Lived in Mount Olympus. Married to Zeus.

outputs:

    <h2><a name="zeus">Zeus</a></h2>
    
    <p>Lived in Mount Olympus. Married to <a href="#hera">Hera</a>.</p>
    
    <h2><a name="hera">Hera</a></h2>
    
    <p>Lived in Mount Olympus. Married to <a href="#zeus">Zeus</a>.</p>

Usage
-----

TBF

License
-------

See LICENSE

Un poco de historia
-------------------

Allá por el año 2000, estuve interesado en la mitología griega. No había
Wikipedia, y cualquier consulta debía hacerla en mi enciclopedia de 24 tomos.
La mitología griega fue el primer culebrón de la Historia, y cualquier 
personaje tenía relación con otros diez. Andar consultando la enciclopedia
en semejante tela de araña se me hacía agotador.

Así que se me ocurrió hacer una página web que reuniera toda esta información.
Recordé que había comprado la misma enciclopedia en digital en ¡6 cds! (y yo 
que pensé que nunca le daría uso...) copié los artículos, y terminé 
implementando un programa que generaba la página web a partir de un fichero de 
texto con todos los artículos.

La página web estuvo colgada durante muchos años en 
http://inicia.es/de/rosogon/mitologia/mitologia.html, y todavía pueden 
encontrarse en google trazos de su existencia. 

Este proyecto es la reencarnación de aquel programa, que constaba de un
script en awk para extraer los títulos de cada artículo y un programa
en lex/yacc para la generación de la página web.

