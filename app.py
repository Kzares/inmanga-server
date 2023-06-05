from flask import Flask, request,send_from_directory
from flask_cors import CORS
from config import config
import os
import ssl

#Routes
from routes import Mangas, Users

app=Flask(__name__,static_folder='static')
CORS(app, resources={r"/*": {"origins": "*"}})


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('/etc/letsencrypt/live/bakteria.online/fullchain.pem', '/etc/letsencrypt/live/bakteria.online/privkey.pem')
######__saving the mangas images
@app.route('/image/<name>', methods=['POST'])
def upload_image(name):
    file = request.files['file'] # file es el nombre del campo en el formulario donde se incluye la imagen
    file.save(os.path.join(app.static_folder, name)) # app.static_folder es la ruta de la carpeta static de Flask, donde se guardar   la imagen con el nombre indicado en el endpoint
    return 'Imagen guardada correctamente'

######__send images
@app.route('/download/<filename>')
def get_image(filename):
    return send_from_directory( 'static' , filename )


def page_not_found(error):
    return '<h1>Page not found</h1>', 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprint
    app.register_blueprint(Mangas.main, url_prefix='/api/mangas' )
    app.register_blueprint(Users.main, url_prefix='/api/users' )


    #error handler
    app.register_error_handler(404, page_not_found)

    app.run(debug=True, ssl_context=context, host='0.0.0.0', port=5000)
