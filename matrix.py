from matrix_client.api import MatrixHttpApi
from datetime import datetime


# SETTINGS:
MORNING = 9   # 9:00
EVENING = 18  # 18:00
SERVER = "https://vmserver.vistamed.ru"  # YOUR_SERVER
TOKEN = "YOUR_TOKEN"
ROOM = "!YOUR_ROOM:vistamed.ru"
# ------------------------------------------------


# MESSAGE:
def sending(message):
    matrix = MatrixHttpApi(SERVER, token=TOKEN)
    response = matrix.send_message(ROOM, message)
    return response
# ------------------------------------------------


# MAIN:
while True:
    now = datetime.now()
    if now.hour == MORNING or now.hour == EVENING \
            and now.minute == 0 and now.second == 0\
            and now.isoweekday() not in [6, 7]:
        sending(now.strftime("%d.%m.%Y %H:%M"))
