const articles = document.querySelector('.articles');

const url = "http://127.0.0.1:5000/api/articles";
// const loginUrl = "http://iv1-21-mvc-rest:8080/api/users/login";
// const userUrl = "http://iv1-21-mvc-rest:8080/api/users";

let responseStatus = 0;

const submitPost = document.querySelector('#submit-post');
const submitLogin = document.querySelector('#submit-login');
// let authData = btoa('q:qqqqqqq');
// let token = '';
// authData ='Basic '+ authData;
authData ='Bearer ';

// let loginForm = document.querySelector('form-login');

// let user = null;
// let helloString =  document.querySelector('.hello-string');
// let userName = document.querySelector('.user-hello');
// let formLogin = document.querySelector('.form-login');

//Получение статей

fetch(url).then(data => data.json()).then(
    data => {
        data.articles.map(createArticle);
        console.log(data);
    }
);


function createArticle(item) {
    const listElement = document.createElement('li');
    listElement.classList.add('main-ul');

    const title = document.createElement('h2');
    title.textContent = item.name;
    const img = document.createElement('img');
    img.src = item.img;
    img.classList.add('img');    const text  = document.createElement('p');
    const buttonDelete  = document.createElement('button');
    text.textContent = item.text;
    const author  = document.createElement('p');
    author.textContent = `Автор: ${item.nickname}`;
    buttonDelete.textContent = 'Удалить статью';
    listElement.appendChild(title);
    listElement.appendChild(img);
    listElement.appendChild(text);
    listElement.appendChild(author);
    // if(user == item.nickname){
    //     listElement.appendChild(buttonDelete);
    // }
    // buttonDelete.addEventListener('click', () => deleteArticle(item.id, listElement))
    articles.appendChild(listElement);
}

console.log('!!!');