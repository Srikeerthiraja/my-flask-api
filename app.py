from flask import Flask, request, jsonify, Response
from collections import OrderedDict
import json
import re
from datetime import datetime

app = Flask(__name__)

FULL_NAME = "john_doe"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

def alternating_caps(s):
    result = []
    upper = True
    for ch in s:
        result.append(ch.upper() if upper else ch.lower())
        upper = not upper
    return "".join(result)

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.get_json()
        arr = data.get("data", [])

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        sum_numbers = 0
        concat_alpha = ""

        for item in arr:
            item_str = str(item)
            if re.fullmatch(r'[0-9]+', item_str):
                num = int(item_str)
                sum_numbers += num
                if num % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
            elif re.fullmatch(r'[a-zA-Z]+', item_str):
                alphabets.append(item_str.upper())
                concat_alpha += item_str
            else:
                special_characters.append(item_str)

        concat_string = alternating_caps(concat_alpha[::-1])
        date_str = datetime.now().strftime("%d%m%Y")
        user_id = f"{FULL_NAME}_{date_str}"

        # Prepare OrderedDict in the exact order required
        response_data = OrderedDict([
            ("is_success", True),
            ("user_id", user_id),
            ("email", EMAIL),
            ("roll_number", ROLL_NUMBER),
            ("odd_numbers", odd_numbers),
            ("even_numbers", even_numbers),
            ("alphabets", alphabets),
            ("special_characters", special_characters),
            ("sum", str(sum_numbers)),
            ("concat_string", concat_string)
        ])

        # Return JSON string to preserve order
        return Response(json.dumps(response_data), mimetype='application/json'), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port =5000)
