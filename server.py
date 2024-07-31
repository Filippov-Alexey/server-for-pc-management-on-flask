from flask import Flask, request, render_template,jsonify
import pyautogui
import keyboard
import time
key_states = {
    'Shift': False,
    'Ctrl': False,
    'Win': False,
    'Alt': False
}

mxy=5

CURSOR_SPEED = 0.5
CURSOR_ACCELERATION = 0.1

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('i.html')

@app.route('/send-text', methods=['POST'])
def send_text():
    if request.method == 'POST':
        dx=0
        dy=0
        button_id = request.json.get('id')
        print(button_id)
        if button_id:
            if button_id=='left':
                pyautogui.click(button='left')
            if button_id=='right':
                pyautogui.click(button='right')
            if button_id=='num-1':
                dx=-mxy
                dy=+mxy
            if button_id=='num-2':
                dy=+mxy
            if button_id=='num-3':
                dx=+mxy
                dy=+mxy
            if button_id=='num-4':
                dx=-mxy
            if button_id=='num-5':
                pyautogui.leftClick()
            if button_id=='num-6':
                dx=+mxy
            if button_id=='num-7':
                dx=-mxy
                dy=-mxy
            if button_id=='num-8':
                dy=-mxy
            if button_id=='num-9':
                dx=+mxy
                dy=-mxy
            pyautogui.moveRel(dx,dy)
            
            if button_id == '~':
                keyboard.press_and_release('~')
            elif button_id == '1':
                keyboard.press_and_release('1')
            elif button_id == '2':
                keyboard.press_and_release('2')
            elif button_id == '3':
                keyboard.press_and_release('3')
            elif button_id == '4':
                keyboard.press_and_release('4')
            elif button_id == '5':
                keyboard.press_and_release('5')
            elif button_id == '6':
                keyboard.press_and_release('6')
            elif button_id == '7':
                keyboard.press_and_release('7')
            elif button_id == '8':
                keyboard.press_and_release('8')
            elif button_id == '9':
                keyboard.press_and_release('9')
            elif button_id == '0':
                keyboard.press_and_release('0')
            elif button_id == '-':
                keyboard.press_and_release('-')
            elif button_id == '=':
                keyboard.press_and_release('=')
            elif button_id == 'Backspace':
                keyboard.press_and_release('backspace')
            elif button_id == 'Tab':
                keyboard.press_and_release('tab')
            elif button_id == 'Q':
                keyboard.press_and_release('q')
            elif button_id == 'W':
                keyboard.press_and_release('w')
            elif button_id == 'E':
                keyboard.press_and_release('e')
            elif button_id == 'R':
                keyboard.press_and_release('r')
            elif button_id == 'T':
                keyboard.press_and_release('t')
            elif button_id == 'Y':
                keyboard.press_and_release('y')
            elif button_id == 'U':
                keyboard.press_and_release('u')
            elif button_id == 'I':
                keyboard.press_and_release('i')
            elif button_id == 'O':
                keyboard.press_and_release('o')
            elif button_id == 'P':
                keyboard.press_and_release('p')
            elif button_id == '[':
                keyboard.press_and_release('[')
            elif button_id == ']':
                keyboard.press_and_release(']')
            elif button_id == '\\':
                keyboard.press_and_release('\\')
            elif button_id == 'CapsLock':
                keyboard.press_and_release('capslock')
            elif button_id == 'A':
                keyboard.press_and_release('a')
            elif button_id == 'S':
                keyboard.press_and_release('s')
            elif button_id == 'D':
                keyboard.press_and_release('d')
            elif button_id == 'F':
                keyboard.press_and_release('f')
            elif button_id == 'G':
                keyboard.press_and_release('g')
            elif button_id == 'H':
                keyboard.press_and_release('h')
            elif button_id == 'J':
                keyboard.press_and_release('j')
            elif button_id == 'K':
                keyboard.press_and_release('k')
            elif button_id == 'L':
                keyboard.press_and_release('l')
            elif button_id == ';':
                keyboard.press_and_release(';')
            elif button_id == "'":
                keyboard.press_and_release("'")
            elif button_id == 'Enter':
                keyboard.press_and_release('enter')
            elif button_id == 'Z':
                keyboard.press_and_release('z')
            elif button_id == 'X':
                keyboard.press_and_release('x')
            elif button_id == 'C':
                keyboard.press_and_release('c')
            elif button_id == 'V':
                keyboard.press_and_release('v')
            elif button_id == 'B':
                keyboard.press_and_release('b')
            elif button_id == 'N':
                keyboard.press_and_release('n')
            elif button_id == 'M':
                keyboard.press_and_release('m')
            elif button_id == ',':
                keyboard.press_and_release(',')
            elif button_id == '.':
                keyboard.press_and_release('.')
            elif button_id == '/':
                keyboard.press_and_release('/')
            elif button_id == 'Shift':
                if key_states['Shift']:
                    keyboard.release('shift')
                else:
                    keyboard.press('shift')
                key_states['Shift'] = not key_states['Shift']
            elif button_id == 'Ctrl':
                if key_states['Ctrl']:
                    keyboard.release('ctrl')
                else:
                    keyboard.press('ctrl')
                key_states['Ctrl'] = not key_states['Ctrl']
            elif button_id == 'Win':
                if key_states['Win']:
                    keyboard.release('win')
                else:
                    keyboard.press('win')
                key_states['Win'] = not key_states['Win']
            elif button_id == 'Alt':
                if key_states['Alt']:
                    keyboard.release('alt')
                else:
                    keyboard.press('alt')
                key_states['Alt'] = not key_states['Alt']
            elif button_id == 'Space':
                keyboard.press_and_release('space')
        return '', 204

last_positions = [(0, 0), (0, 0)]


@app.route('/touchpad', methods=['POST'])
def handle_touchpad():
    data = request.get_json()
    if 'dx' in data:
        # 触摸板数据
        dx = data['dx']
        dy = data['dy']
        is_end = data['isEnd']

        print(f'Touchpad delta: ({dx}, {dy}), IsEnd: {is_end}')

        # 更新鼠标位置
        update_mouse_position(dx, dy)

    elif 'leftButton' in data or 'rightButton' in data:
        # 按钮数据
        left_button = data.get('leftButton', False)
        right_button = data.get('rightButton', False)

        print(f'Button state: Left={left_button}, Right={right_button}')

    return jsonify({'status': 'success'}), 200

def update_mouse_position(dx, dy):
    global last_mouse_position,i
    print(dx,dy)
    if dx==0 and dy==0:
        if i==0:
            i=1
        else:
            i=0
        if i==1:
            pyautogui.click(button='left')

    current_x, current_y = pyautogui.position()
    new_x = current_x + dx
    new_y = current_y + dy
    pyautogui.moveTo(new_x, new_y, duration=CURSOR_SPEED)
    
    last_mouse_position = (new_x, new_y)

i=0
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
