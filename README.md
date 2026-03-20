Alke Wallet
Proyecto final del Módulo 7 - Desarrollo Web con Django  
Autor: Mario Heredia

¿Qué es Alke Wallet?

Aplicación web de billetera digital desarrollada con Django. Permite gestionar clientes, cuentas y transacciones mediante operaciones CRUD, autenticación de usuarios y panel de administración.

Tecnologías utilizadas

- Python 3.12
- Django 6.0
- SQLite (desarrollo)
- HTML + CSS (archivos estáticos)
- Git + GitHub


Como ejecutar el proyecto localmente

1. Clonar el repositorio:
   git clone git@github.com:MarioHerediaM/alke-wallet.git
   cd alke-wallet

2. Crear y activar el entorno virtual:
   python -m venv venv
   source venv/bin/activate

3. Instalar dependencias:
   pip install django

4. Aplicar migraciones:
   python manage.py migrate

5. Crear superusuario:
   python manage.py createsuperuser

6. Levantar el servidor:
   python manage.py runserver

7. Abrir en el navegador:
   http://127.0.0.1:8000/clientes/

---

Configuración de la base de datos

Para desarrollo se usa SQLite, configurado por defecto en settings.py.
Para producción se puede usar PostgreSQL instalando psycopg2 y configurando
NAME, USER, PASSWORD, HOST y PORT en el bloque DATABASES de settings.py.

Modelos definidos

- Cliente: nombre, email, teléfono, dirección.
- Cuenta: número de cuenta, relación ForeignKey con Cliente.
- Transaccion: tipo, monto, fecha, relación ForeignKey con Cuenta.

Operaciones CRUD

Se implementaron vistas basadas en clases (ListView, CreateView, UpdateView, DeleteView) para el modelo Cliente, con formularios protegidos con token CSRF y rutas dinámicas usando <int:pk>.

Consultas personalizadas realizadas

Desde la shell interactiva se practicaron:
- Cliente.objects.all()
- Cliente.objects.filter(nombre__istartswith='A')
- Cliente.objects.exclude(email="...")
- Cliente.objects.raw("SELECT * FROM gestion_cliente WHERE telefono IS NOT NULL")
- Consulta directa con connection.cursor()

Aplicaciones preinstaladas utilizadas

- django.contrib.admin → panel de administración en /admin
- django.contrib.auth → login y logout en /accounts/login/
- django.contrib.staticfiles → sirve el archivo static/style.css

Reflexiones

El ORM de Django simplifica enormemente el acceso a la base de datos, 
permitiendo hacer consultas sin escribir SQL directamente. Las migraciones 
mantienen un historial versionado de los cambios en los modelos, lo que 
facilita el trabajo en equipo. La integración de consultas personalizadas 
con raw() y cursores es útil cuando se necesita mayor control sobre las consultas.

 Estructura del repositorio en GitHub

- main → código estable y completo
- feature/modelos → rama para desarrollo de modelos
- feature/crud → rama para desarrollo de vistas y formularios