// 用户发送消息
const input = document.querySelector('.input');
const sendButton = document.querySelector('.send-button');
const messages = document.querySelector('.messages');
const chatWindow = document.querySelector('.chat-window');

function sendMessage() {
    const messageText = input.value.trim();

    if (messageText === '') {
        return;
    }

    const message = document.createElement('div');
    message.classList.add('messageUserSend');
    message.textContent = messageText;

    messages.appendChild(message);
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // 演示服务器发送消息
    const childDivs = messages.querySelectorAll('div');
    console.log(childDivs.length);

    const yourmessage = document.createElement('div');
    yourmessage.classList.add('messageServerSend');
    yourmessage.textContent = "hello world!";
    messages.appendChild(yourmessage);
    chatWindow.scrollTop = chatWindow.scrollHeight;
    // 演示服务器发送消息

    input.value = '';
    input.style.height = '16px';
}

sendButton.addEventListener('click', sendMessage);



// 动态调整输入框大小
input.addEventListener('input', (event) => {
    input.style.height = '16px';
    if (event.target.scrollHeight + 'px' < '40px') {
        input.style.height = event.target.scrollHeight + 'px';
    } else {
        input.style.height = '40px';
    }
});



// 阻止回车换行，执行回车=submit
input.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});


// 输入框左侧菜单按钮
const menuButton = document.querySelector('.menu-button');

function menuControl() {
    document.getElementById("myMenu").classList.toggle("show-menu");
    menuButton.classList.toggle("menu-button-vary");
};

menuButton.addEventListener('click', menuControl);

// 菜单内部弹窗按钮
const openPopup = document.getElementById("strawberry");
const confirmButton = document.querySelector('.confirm');
const cancelButton = document.querySelector('.cancel');

function confirmContrl() {
    document.getElementById("popup").classList.toggle("popup");
}
// 打开
openPopup.addEventListener('click', confirmContrl);
// 确认
confirmButton.addEventListener('click', confirmContrl);
// 取消
cancelButton.addEventListener('click', confirmContrl);