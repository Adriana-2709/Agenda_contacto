# 📒 Agenda de Contactos

Un programa sencillo para **guardar los números de teléfono de tus contactos**, como la agenda de un celular pero en la computadora.

## ¿Qué hace?

Al ejecutarlo, aparece un menú donde puedes elegir qué quieres hacer:

1. **Agregar un contacto:** escribes el nombre y el teléfono, y se guarda.
2. **Ver todos los contactos:** te muestra la lista completa con sus números.
3. **Buscar un contacto:** escribes un nombre y te dice su teléfono.
4. **Eliminar un contacto:** borras a alguien que ya no necesitas.
5. **Salir:** cierra el programa.

## ¿Cómo guarda la información?

Usa un **diccionario**, que funciona igual que una agenda de papel: cada nombre tiene su número al lado.

```
Ana Pérez  →  0991234567
Luis Mora  →  0987654321
```

## ¿Cómo se usa?

1. Instala [Python](https://www.python.org/downloads/) si aún no lo tienes.
2. Descarga el archivo `agenda_contactos.py`.
3. Ábrelo con el programa y ejecútalo, o escribe en la terminal:

   ```
   python agenda_contactos.py
   ```

4. Sigue las opciones del menú escribiendo el número que quieras y presionando Enter.

## Ejemplo

```
===== AGENDA =====
1. Agregar contacto
2. Mostrar contactos
3. Buscar contacto
4. Eliminar contacto
5. Salir
Elige una opción: 1
Nombre del contacto: Ana Pérez
Número telefónico: 0991234567
Contacto 'Ana Pérez' agregado correctamente.
```

## Nota

Los contactos se guardan solo mientras el programa está abierto. Al cerrarlo, la agenda queda vacía otra vez.
