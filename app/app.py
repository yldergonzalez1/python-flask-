from flask import Flask, render_template
app= Flask (__name__)
@app.route("/")
def inicio():
  propiedades_pagina={
    'titulo_en_tab': 'Soy Empresario - Todo a tu alcance',
    'titulo':'Soy Empresario',
    'slogan': 'Contacta y Compra!'
  }
  return render_template('inicio.html', propiedades_pagina=propiedades_pagina)

@app.route("/contacto")
def contacto():
  return render_template('contacto.html')

@app.route("/python")
def python():
  return render_template('python.html')

def pagina_no_encontrada(error):
  return render_template ('404.html'), 404

if __name__=='__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
