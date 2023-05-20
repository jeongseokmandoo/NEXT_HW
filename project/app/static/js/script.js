var questions = [
  {
    id: 0,
    text: "지친 나를 위로해주는 것은?",
    type: "SA",
    choices: ["콘서트🎉", "친구들과의 술자리🍺"],
    points: [1, 0],
  },
  {
    id: 1,
    text: "나는 새로운 장소에 갔을 때?",
    type: "LF",
    choices: ["새로운 친구를 사겨볼래👯", "운명적 사랑을 찾아볼래💏"],
    points: [1, 0],
  },
  {
    id: 2,
    text: "내가 가려는 맛집이 웨이팅을 해야하는 식당이라면?",
    type: "EU",
    choices: ["웨이팅 해서라도 경험해볼래!🏋️", "웨이팅은 못해…💦"],
    points: [1, 0],
  },
  {
    id: 3,
    text: "애인과 하고 싶은 데이트는?",
    type: "SA",
    choices: ["공연보러 가기🎸", "오붓하게 술 한 잔 하기🍷"],
    points: [1, 0],
  },
  {
    id: 4,
    text: "지금 더 만들고 싶은 인간 관계는?",
    type: "LF",
    choices: ["친구👯", "연인💏"],
    points: [1, 0],
  },
  {
    id: 5,
    text: "내가 더 좋아하는 술자리는?",
    type: "PC",
    choices: ["술 게임을 하는 자리🕹️", "딥토크를 하는 자리💬"],
    points: [1, 0],
  },
  {
    id: 6,
    text: "대동제에서 가장 기대되는 것은?",
    type: "SA",
    choices: ["연예인들 라인업🎫", "동기들과 함께 하는 주점🐾"],
    points: [1, 0],
  },
  {
    id: 7,
    text: "더 좋아하는 음악 장르는?",
    type: "PC",
    choices: ["힙합🎧", "발라드🎵"],
    points: [1, 0],
  },

  {
    id: 8,
    text: "콘서트나 공연을 보기 위해 기다리는 시간이 나는?",
    type: "EU",
    choices: ["괜찮아!👍", "아깝다ㅠㅠ😭"],
    points: [1, 0],
  },
  {
    id: 9,
    text: "저녁을 먹고 가야하는 장소를 고른다면?",
    type: "PC",
    choices: ["춘자", "카페☕️"],
    points: [1, 0],
  },
  {
    id: 10,
    text: "나는 좋아하는 걸 위해 =>",
    type: "EU",
    choices: ["꽤 긴 시간을 기다릴 수 있다🙆", "기다리기 싫어!🙅"],
    points: [1, 0],
  },
  {
    id: 11,
    text: "내가 생각하는 미팅의 목적은?",
    type: "LF",
    choices: ["재미있는 분위기🥳", "이성과의 만남🥰"],
    points: [1, 0],
  },
];

var currentQuestionIndex = 0;
var questionSection = document.getElementById("questionSection");
var questionTitle = document.getElementById("questionTitle");
var questionText = document.getElementById("questionText");
var choicesSection = document.getElementById("choicesSection");
var nextButton = document.getElementById("nextButton");
var prevButton = document.getElementById("prevButton");
var scoreSA = 0;
var scorePC = 0;
var scoreEU = 0;
var scoreLF = 0;
// Added totalScore variable

function displayQuestion() {
  var currentQuestion = questions[currentQuestionIndex];
  questionTitle.textContent = "Question " + (currentQuestionIndex + 1);
  questionText.textContent = currentQuestion.text;

  choicesSection.innerHTML = ""; // Clear previous choices

  currentQuestion.choices.forEach(function (choice, idx) {
    var choiceElement = document.createElement("input");
    choiceElement.setAttribute("type", "radio");
    choiceElement.setAttribute("name", "answer");
    choiceElement.setAttribute("id", `answerInput_${idx}`);
    choiceElement.setAttribute("value", choice);

    var choiceLabel = document.createElement("label");
    choiceLabel.setAttribute("for", `answerInput_${idx}`);
    choiceLabel.setAttribute("name", "answerLabel");
    choiceLabel.textContent = choice;

    var choiceContainer = document.createElement("div");
    choiceContainer.appendChild(choiceElement);
    choiceContainer.appendChild(choiceLabel);

    choicesSection.appendChild(choiceContainer);
  });
}

function handleNextButtonClick() {
  // Get the selected choice
  var selectedChoice = document.querySelector('input[name="answer"]:checked');
  var answer = selectedChoice.value;

  if (selectedChoice) {
    console.log("Selected answer:", answer);

    // Calculate the points for the current question
    var currentQuestion = questions[currentQuestionIndex];
    var points =
      currentQuestion.points &&
      currentQuestion.points[currentQuestion.choices.indexOf(answer)];

    if (currentQuestion.type === "SA") {
      scoreSA += points || 0;
    } else if (currentQuestion.type === "PC") {
      scorePC += points || 0;
    } else if (currentQuestion.type === "EU") {
      scoreEU += points || 0;
    } else if (currentQuestion.type === "LF") {
      scoreLF += points || 0;
    }
    // Add the points to the user's total score

    // Move to the next question
    currentQuestionIndex++;

    // Check if there are more questions
    if (currentQuestionIndex < questions.length) {
      displayQuestion();
    } else {
      // No more questions, survey completed

      // Classify the user based on the total score
      var classification1 = "";
      if (scoreSA >= 2 && scoreSA <= 3) {
        classification1 = "S";
      } else if (scoreSA >= 0 && scoreSA <= 1) {
        classification1 = "A";
      }

      var classification2 = "";
      if (scorePC >= 2 && scorePC <= 3) {
        classification2 = "P";
      } else if (scorePC >= 0 && scorePC <= 1) {
        classification2 = "C";
      }

      var classification3 = "";
      if (scoreEU >= 2 && scoreEU <= 3) {
        classification3 = "E";
      } else if (scoreEU >= 0 && scoreEU <= 1) {
        classification3 = "U";
      }

      var classification4 = "";
      if (scoreLF >= 2 && scoreLF <= 3) {
        classification4 = "F";
      } else if (scoreLF >= 0 && scoreLF <= 1) {
        classification4 = "L";
      }

      var classification =
        classification1 + classification2 + classification3 + classification4;

      // Redirect to the result page with the classification as a parameter
      window.location.href = "result/" + classification + "/";
    }
  } else {
    alert("Please select an answer.");
  }
}

function handlePrevButtonClick() {
  currentQuestionIndex--;
  if (currentQuestionIndex >= 0) {
    displayQuestion();
  } else {
    currentQuestionIndex = 0;
  }
}
// Attach event listener to the next button
nextButton.addEventListener("click", handleNextButtonClick);
prevButton.addEventListener("click", handlePrevButtonClick);

// Initial question display
displayQuestion();