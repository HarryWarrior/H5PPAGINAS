
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
    