const todoForm = document.getElementById("todo-form");
const todoList = document.getElementById("todo-list");
const submitBtn = document.querySelector(".submitBtn");
const inputBtn = document.querySelector(".inputBtn");

const todos = "TODOS";
let todoLi = [];

function paintTodo(e) {
    const li = document.createElement("li");
    li.id = e.id;
    const span = document.createElement("span");
    const btn = document.createElement('button');

    span.innerHTML = e.text;
    btn.innerHTML = "X";
    btn.addEventListener("click", deleteTodo);

    todoList.appendChild(li);
    li.appendChild(span);
    li.appendChild(btn);
};

function submitAddTodo(event) {
	event.preventDefault();

    const todo = inputBtn.value;
    const it = {
        text : todo,
        id : Date.now()
    };

    todoLi.push(it);
    console.log(todoLi);

    inputBtn.value = "";

    paintTodo(it);
    saveTodos(todoLi);
};

todoForm.addEventListener("submit", submitAddTodo);

function deleteTodo(event) {
    const li = event.target.parentElement;
    li.remove();

    // let newtodoLi = window.localStorage.getItem(todos);   
    todoLi = todoLi.filter(todo => todo.id != parseInt(li.id));
    console.log(todoLi);

    saveTodos(todoLi)
};

function saveTodos(e) {
    window.localStorage.setItem(todos, JSON.stringify(e));
};

const todotodo = localStorage.getItem(todos);

if(todotodo != null) {
    const tdtd = JSON.parse(todotodo);
    todoLi = tdtd;
    todoLi.forEach(e => paintTodo(e));
};