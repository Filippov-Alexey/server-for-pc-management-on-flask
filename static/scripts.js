// Obtain all buttons
const buttons = document.querySelectorAll('button');

// Track the currently pressed button
let pressedButtonId = null;

// Add event listeners to each button
buttons.forEach((btn) => {
    btn.addEventListener('touchstart', (e) => {
        e.preventDefault();
        pressedButtonId = e.currentTarget.id;
    });

    btn.addEventListener('touchend', (e) => {
        e.preventDefault();
        pressedButtonId = null;
    });
});

// Check for pressed buttons every 100 milliseconds and send the ID to the server
setInterval(() => {
    if (pressedButtonId !== null) {
        sendButtonClick(pressedButtonId);
    }
}, 100);

function sendButtonClick(id) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/send-text');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 204) {
            console.log(`Sent button id: ${id}`);
        } else {
            console.error(`Error sending button id: ${id}`);
        }
    };
    xhr.onerror = function() {
        console.error(`Error sending button id: ${id}`);
    };
    xhr.send(JSON.stringify({ id: id }));
}

const num = document.querySelector('.num');
const keyboard = document.querySelector('.keyboard');
const tach = document.querySelector('.cont');

document.addEventListener('click', (event) => {
    if (event.target.id === 'nmlk') {
        if (num.classList.contains('active')) {
            num.classList.remove('active');
            keyboard.classList.add('active');
            tach.classList.add('active');
        } else {
            num.classList.add('active');
            keyboard.classList.remove('active');
            tach.classList.remove('active');
        }
    }
});

document.addEventListener('touchstart', (event) => {
    if (event.target.id === 'nmlk') {
        if (num.classList.contains('active')) {
            num.classList.remove('active');
            keyboard.classList.add('active');
            tach.classList.add('active');
        } else {
            num.classList.add('active');
            keyboard.classList.remove('active');
            tach.classList.remove('active');
        }
    }
});

const touchpad = document.querySelector('.touchpad');
const touchpadCursor = document.querySelector('.touchpad-cursor');
const touchpadXElement = document.getElementById('touchpad-x');
const touchpadYElement = document.getElementById('touchpad-y');
const touchpadClickElement = document.getElementById('touchpad-click');
const leftButton = document.getElementById('left');
const rightButton = document.getElementById('right');

let isLeftButtonPressed = false;
let isRightButtonPressed = false;
let lastTouchPosition = { x: 0, y: 0 };
let touchpadRect = touchpad.getBoundingClientRect();

touchpad.addEventListener('touchstart', (event) => {
    touchpadRect = touchpad.getBoundingClientRect();
    lastTouchPosition = {
        x: event.touches[0].clientX - touchpadRect.left,
        y: event.touches[0].clientY - touchpadRect.top
    };
    updateTouchpadInfo();
    sendTouchpadData();
    updateCursorPosition();
});

touchpad.addEventListener('touchmove', (event) => {
    let newX = event.touches[0].clientX - touchpadRect.left;
    let newY = event.touches[0].clientY - touchpadRect.top;

    // Ограничиваем координаты X и Y
    newX = Math.max(0, Math.min(newX, touchpadRect.width));
    newY = Math.max(0, Math.min(newY, touchpadRect.height));

    const dx = newX - lastTouchPosition.x;
    const dy = newY - lastTouchPosition.y;

    lastTouchPosition = {
        x: newX,
        y: newY
    };

    updateTouchpadInfo();
    sendTouchpadData(dx, dy);
    updateCursorPosition();
});

touchpad.addEventListener('touchend', () => {
    updateTouchpadInfo();
    sendTouchpadData(0, 0, true);
});

leftButton.addEventListener('mousedown', () => {
    isLeftButtonPressed = true;
    sendButtonData(true, false);
});

leftButton.addEventListener('mouseup', () => {
    isLeftButtonPressed = false;
    sendButtonData(false, false);
});

rightButton.addEventListener('mousedown', () => {
    isRightButtonPressed = true;
    sendButtonData(false, true);
});

rightButton.addEventListener('mouseup', () => {
    isRightButtonPressed = false;
    sendButtonData(false, false);
});

window.addEventListener('resize', () => {
    touchpadRect = touchpad.getBoundingClientRect();
});

function updateTouchpadInfo() {
    touchpadXElement.textContent = Math.round(lastTouchPosition.x);
    touchpadYElement.textContent = Math.round(lastTouchPosition.y);
}

function sendTouchpadData(dx, dy, isEnd = false) {
    sendData({
        dx: dx,
        dy: dy,
        isEnd: isEnd
    });
}

function sendButtonData(leftButton, rightButton) {
    sendData({
        leftButton: leftButton,
        rightButton: rightButton
    });
}

function sendData(data) {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/touchpad', false); // устанавливаем synchronous режим
    xhr.setRequestHeader('Content-Type', 'application/json');
    try {
        xhr.send(JSON.stringify(data));
        if (xhr.status === 200) {
            console.log('Touchpad data sent successfully');
        } else {
            console.error('Error sending touchpad data');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

function updateCursorPosition() {
    let x = lastTouchPosition.x;
    let y = lastTouchPosition.y;

    const touchpadWidth = touchpadRect.width;
    const touchpadHeight = touchpadRect.height;

    x = Math.max(0, Math.min(x, touchpadWidth));
    y = Math.max(0, Math.min(y, touchpadHeight));

    touchpadCursor.style.left = `${x}px`;
    touchpadCursor.style.top = `${y}px`;
}
