import os
import json
from jinja2 import Template

def process_content_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    questions = []
    if 'content' in data:
        for item in data['content']:
            if 'params' in item['content']:
                if 'questions' in item['content']['params']:
                    for question in item['content']['params']['questions']:
                        if isinstance(question['params'], dict) and 'question' in question['params'] and 'answers' in question['params']:
                            q_text = question['params']['question']
                            answers = [{'text': answer['text'], 'correct': answer['correct']} for answer in question['params']['answers']]
                            questions.append({'question': q_text, 'answers': answers})
    
    if questions:
        return questions
    else:
        return None

def generate_html_js_css(questions, json_file):
    exercise_folder = os.path.dirname(json_file)
    exercise_name = os.path.basename(exercise_folder)

    html_content = generate_html(exercise_name, questions)
    html_file = os.path.join(exercise_folder, 'index.html')
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    js_content = generate_js()
    js_file = os.path.join(exercise_folder, 'exercise.js')
    with open(js_file, 'w', encoding='utf-8') as file:
        file.write(js_content)

    css_content = generate_css()
    css_file = os.path.join(exercise_folder, 'styles.css')
    with open(css_file, 'w', encoding='utf-8') as file:
        file.write(css_content)

    print(f"Ejercicio generado en: {exercise_folder}")

def generate_html(exercise_name, questions):
    template_str = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ exercise_name }}</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div id="exercise-container">
            <h1 class="exercise-title">{{ exercise_name }}</h1>
            {% for question in questions %}
            <div class="question" data-question-index="{{ loop.index0 }}">
                <p>{{ question.question }}</p>
                <ul>    
                    {% set question_index = loop.index0 %}
                    {% for answer in question.answers %}
                    <li>
                        <label>
                            <input type="radio" name="question{{ question_index }}" value="{{ answer.correct }}">
                            {{ answer.text }}
                        </label>
                    </li>
                    {% endfor %}
                </ul>
            </div>
            {% endfor %}
        </div>
        <button id="check-button">Verificar Respuestas</button>
        <p id="result"></p>
        <script src="exercise.js"></script>
    </body>
    </html>
    """
    template = Template(template_str)
    return template.render(exercise_name=exercise_name, questions=questions)

def generate_js():
    template_str = """
    document.addEventListener('DOMContentLoaded', function () {
        var checkButton = document.getElementById('check-button');
        var result = document.getElementById('result');
        
        checkButton.addEventListener('click', function () {
            var questions = document.querySelectorAll('.question');
            var correctAnswers = 0;
            var totalQuestions = questions.length;
            
            questions.forEach(function (question) {
                var selectedAnswer = question.querySelector('input[type="radio"]:checked');
                
                if (selectedAnswer && selectedAnswer.value === 'True') {
                    correctAnswers++;
                }
            });
            
            result.textContent = 'Respuestas correctas: ' + correctAnswers + ' de ' + totalQuestions;
        });
    });
    """
    template = Template(template_str)
    return template.render()

def generate_css():
    css_content = """
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        color: #333;
        margin: 0;
        padding: 20px;
    }

    .exercise-title {
        text-align: center;
        color: #a52a2a;
    }

    .question {
        margin-bottom: 20px;
    }

    .question p {
        font-weight: bold;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        margin-bottom: 10px;
    }

    #check-button {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #a52a2a;
        color: white;
        border: none;
        cursor: pointer;
    }

    #check-button:hover {
        background-color: #7f1f1f;
    }

    #result {
        text-align: center;
        font-size: 1.2em;
        color: #333;
        margin-top: 20px;
    }
    """
    return css_content

def generate_main_index(exercises):
    template_str = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ejercicios</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div id="main-container">
            <h1 class="main-title">Lista de Ejercicios</h1>
            <ul>
                {% for exercise in exercises %}
                <li><a href="{{ exercise }}/index.html">{{ exercise }}</a></li>
                {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    """
    template = Template(template_str)
    html_content = template.render(exercises=exercises)
    return html_content

folder_path = 'h5p-content-json'
exercise_folders = []

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.json') and file == 'content.json':
            json_file_path = os.path.join(root, file)
            exercise_folder = os.path.relpath(root, folder_path)
            try:
                questions = process_content_json(json_file_path)
                if questions:
                    generate_html_js_css(questions, json_file_path)
                    exercise_folders.append(exercise_folder)
            except Exception as e:
                print(f"Error procesando {json_file_path}: {e}")

main_index_html = generate_main_index(exercise_folders)
main_index_file = os.path.join(folder_path, 'index.html')
with open(main_index_file, 'w', encoding='utf-8') as file:
    file.write(main_index_html)

print(f"Página principal generada en: {main_index_file}")
