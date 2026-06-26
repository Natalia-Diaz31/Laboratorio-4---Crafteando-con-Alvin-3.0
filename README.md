API TecnoMarket con Flask
-------------------------
API creada en clase para practicar Flask, Postman, requests y Git/GitHub.
Permite consultar productos, buscar un producto por código y agregar nuevos productos.

Instalación
------------
python -m venv .venv .venv\Scripts\Activate.ps1 python -m pip install -r requirements.txt

Ejecutar servidor
-----------------
python app.py

Probar endpoints
-----------------

GET http://127.0.0.1:5000/productos

GET http://127.0.0.1:5000/productos/201

POST http://127.0.0.1:5000/productos
