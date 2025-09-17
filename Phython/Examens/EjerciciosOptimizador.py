from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# --- CONFIGURACIÓN ---
capitulos = {
    1: "Introducción a los algoritmos",
    2: "Algoritmos de ordenación",
    3: "Técnicas de diseño de algoritmos",
    4: "Problemas tipo",
    5: "Algoritmos de búsqueda",
    6: "Descenso del gradiente",
    7: "Métodos heurísticos y metaheurísticos",
    8: "Algoritmos evolutivos y genéticos"
}

# --- GENERADOR DE PREGUNTAS ---
def generar_preguntas():
    preguntas = []
    id_counter = 0
    for cap in range(1, 9):
        for i in range(1, 6):  # 5 preguntas por capítulo
            tema = capitulos[cap]
            opciones = [
                f"A) Opción incorrecta sobre {tema.lower()}",
                f"B) Otra opción irrelevante",
                f"C) Una posible confusión común",
                f"D) Respuesta correcta relacionada con {tema.lower()}"
            ]
            correcta = "D"
            random.shuffle(opciones)
            preguntas.append({
                'id': id_counter,
                'texto': f"(Cap. {cap}) ¿Cuál es la opción correcta sobre: {tema} ({i})?",
                'opciones': opciones,
                'correcta': correcta
            })
            id_counter += 1
    random.shuffle(preguntas)
    return preguntas[:40]

# --- PLANTILLA HTML ---
template = """
<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <title>Simulacro de Examen</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        .pregunta { background: #f9f9f9; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
        button { background-color: #074f0f; color: white; padding: 10px 20px; border: none; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Simulacro de Examen - Algoritmos</h1>
    <form method="post">
        {% for p in preguntas %}
        <div class="pregunta">
            <p><strong>{{ loop.index }}. {{ p.texto }}</strong></p>
            {% for opcion in p.opciones %}
                <label><input type="radio" name="pregunta{{ p.id }}" value="{{ opcion[0] }}"> {{ opcion }}</label><br>
            {% endfor %}
        </div>
        {% endfor %}
        <button type="submit">Enviar respuestas</button>
    </form>
    {% if resultado is defined %}
    <h2>Resultado final: {{ resultado }} / {{ total }} correctas</h2>
    <p>Puntaje: {{ porcentaje }}%</p>
    {% endif %}
</body>
</html>
"""

# --- RUTA PRINCIPAL ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        respuestas = request.form
        correctas = 0
        total = len(preguntas_global)
        for p in preguntas_global:
            seleccion = respuestas.get(f'pregunta{p["id"]}', '')
            if seleccion == p['correcta']:
                correctas += 1
        porcentaje = round((correctas / total) * 100, 2)
        return render_template_string(template, preguntas=preguntas_global, resultado=correctas, total=total, porcentaje=porcentaje)

    global preguntas_global
    preguntas_global = generar_preguntas()
    return render_template_string(template, preguntas=preguntas_global)

# --- INICIO DE APLICACIÓN ---
if __name__ == '__main__':
    app.run(debug=True)
