document.addEventListener("DOMContentLoaded", function() {
    // JSON proporcionado
    var jsonContent = {
        "content": [
            {
                "content": {
                    "params": {
                        "questions": [
                            {
                                "question": "¿Qué bibliotecas externas se utilizan en este código y para qué propósito?",
                                "answers": [
                                    {
                                        "text": "WiFi.h, PubSubClient.h, OneWire.h y DallasTemperature.h",
                                        "correct": true
                                    },
                                    {
                                        "text": "WiFi.h, Bluetooth.h, LiquidCrystal.h",
                                        "correct": false
                                    },
                                    {
                                        "text": "ESP32WiFi.h, MQTTClient.h, Servo.h",
                                        "correct": false
                                    }
                                ]
                            },
                            {
                                "question": "¿Cuál es la función de `setup_wifi()` en este código?",
                                "answers": [
                                    {
                                        "text": "Establece la conexión Wi-Fi con el nombre de red y la contraseña proporcionados",
                                        "correct": true
                                    },
                                    {
                                        "text": "Configura el servidor MQTT y el cliente",
                                        "correct": false
                                    },
                                    {
                                        "text": "Inicializa el sensor de temperatura",
                                        "correct": false
                                    }
                                ]
                            },
                            {
                                "question": "¿Qué hace la función `reconnect()`?",
                                "answers": [
                                    {
                                        "text": "Intenta conectarse al servidor MQTT en caso de que la conexión se pierda",
                                        "correct": true
                                    },
                                    {
                                        "text": "Reinicia el ESP32 en caso de falla",
                                        "correct": false
                                    },
                                    {
                                        "text": "Reinicia la conexión Wi-Fi si se pierde",
                                        "correct": false
                                    }
                                ]
                            },
                            {
                                "question": "¿Cuál es el propósito de `sensors.requestTemperatures()` en el código?",
                                "answers": [
                                    {
                                        "text": "Solicita al sensor DS18B20 que tome una lectura de temperatura",
                                        "correct": true
                                    },
                                    {
                                        "text": "Configura el pin de datos del sensor",
                                        "correct": false
                                    },
                                    {
                                        "text": "Lee la temperatura actual del sensor",
                                        "correct": false
                                    }
                                ]
                            },
                            {
                                "question": "¿Por qué se verifica `isnan(temperatura)` después de leer la temperatura del sensor?",
                                "answers": [
                                    {
                                        "text": "Para detectar si la lectura del sensor produjo un valor inválido o no numérico",
                                        "correct": true
                                    },
                                    {
                                        "text": "Para verificar si la conexión Wi-Fi está activa",
                                        "correct": false
                                    }
                                ]
                            }
                        ]
                    }
                },
                "useSeparator": "auto"
            }
        ]
    };

    var exerciseContainer = document.getElementById('exercise-container');
    
    // Función para generar el contenido del ejercicio
    function generateExercise() {
        var questions = jsonContent.content[0].content.params.questions;

        // Iterar sobre cada pregunta
        questions.forEach(function(questionObj, index) {
            var questionDiv = document.createElement('div');
            questionDiv.classList.add('question');

            var questionText = document.createElement('p');
            questionText.textContent = (index + 1) + '. ' + questionObj.question;
            questionDiv.appendChild(questionText);

            // Iterar sobre las respuestas de cada pregunta
            questionObj.answers.forEach(function(answerObj, answerIndex) {
                var answerLabel = document.createElement('label');
                var answerInput = document.createElement('input');
                answerInput.setAttribute('type', 'radio');
                answerInput.setAttribute('name', 'question' + index);
                answerInput.setAttribute('value', answerIndex);

                answerLabel.appendChild(answerInput);
                answerLabel.appendChild(document.createTextNode(answerObj.text));
                questionDiv.appendChild(answerLabel);
            });

            exerciseContainer.appendChild(questionDiv);
        });
    }

    // Llamar a la función para generar el ejercicio
    generateExercise();

    // Agregar evento al botón de verificación
    var checkButton = document.getElementById('check-button');
    checkButton.addEventListener('click', function() {
        var correctAnswers = 0;

        // Iterar sobre las respuestas seleccionadas y contar las correctas
        var questions = document.getElementsByClassName('question');
        for (var i = 0; i < questions.length; i++) {
            var inputs = questions[i].querySelectorAll('input[type="radio"]');
            for (var j = 0; j < inputs.length; j++) {
                if (inputs[j].checked) {
                    if (jsonContent.content[0].content.params.questions[i].answers[j].correct) {
                        correctAnswers++;
                    }
                    break; // Salir del bucle interno una vez que se encuentra la respuesta seleccionada
                }
            }
        }

        // Mostrar el resultado
        alert('Respuestas correctas: ' + correctAnswers + '/' + questions.length);
    });
});
