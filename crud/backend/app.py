from flask import Flask
from flask_cors import CORS
from flask import jsonify,request
import pymysql

app=Flask(__name__)
## nos permite acceder desde una api externa
CORS(app)
##funciona para conectarnos a la base de datos de mysql
def conectar(vhost,vuser,vpass,vdb):
    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
    return conn
# ruta para consulta generañ
@app.route("/")
def consulta_general():
    try:
        conn = conectar('localhost','root','','gestor_contrasena')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM baul""")
        datos = cur.fetchall()
        data=[]
        for row in datos:
            dato={'id_baul': row[0],'Plataforma':row[1],'usuario':row[2],'clave':row[3]}
            data.append(dato)
        cur.close()
        conn.close()
        return jsonify({'baul':data,'mensaje':'Baul de contraseñas'})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})

## consulta individual
@app.route("/consulta_individual/<codigo>",methods=['GET'])
def consulta_individual(codigo):
    try:
        conn = conectar('localhost','root','','gestor_contrasena')
        cur = conn.cursor()
        cur.execute("""SELECT * FROM baul""")
        datos=cur.fetchone()
        cur.close()
        conn.close()
        if datos!=None:
             dato={'id_baul': row[0],'Plataforma':row[1],'usuario':row[2],'clave':row[3]}
             return jsonify({'baul':dato,'mensaje':'Registro encontrado'})
        else:
            return jsonify({'mensjae':'Registro no encontrado'})
    except Exception as ex:
        return jsonify({'mensaje':'Error'})

## registro
@app.route("/registro/", methods=['POST'])
def registro():
    try:
        conn = conectar('localhost', 'root', '', 'gestor_contrasena')
        cur = conn.cursor()
        x = cur.execute("""INSERT INTO baul (plataforma, usuario, clave) VALUES\
                         ('{0}', '{1}', '{2}')""".format(
            request.json['plataforma'],
            request.json['usuario'],
            request.json['clave']
        ))
        conn.commit()  # para confirmar la inserción de la información
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro agregado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})
    
# Ruta para eliminar un registro por código
@app.route("/eliminar/<codigo>", methods=['DELETE'])
def eliminar(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'gestor_contrasena')
        cur = conn.cursor()
        cur.execute("""delete from baul WHERE id_baul ={0}""".format (codigo,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Eliminado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Ruta para actualizar un registro por código
@app.route("/actualizar/<codigo>", methods=['PUT'])
def actualizar(codigo):
    try:
        conn = conectar('localhost', 'root', '', 'gestor_contrasena')
        cur = conn.cursor()
        x=cur.execute("""update baul set plataforma = '{0}',usuario ='{1}',clave ='{2}' WHERE \
                       id_baul ={3}""".format(request.json['plataforma'], request.json['usuario'], request.json['clave'], codigo))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)



                 

            
            
