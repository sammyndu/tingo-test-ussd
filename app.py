from flask import Flask, request, make_response

app = Flask(__name__)

response = ""

@app.route("/", methods=["GET", "POST"])
def home():
    global response
    sessionId = request.values.get('sessionId')
    service_code = request.values.get("serviceCode")
    phone_number = request.values.get("phoneNumber")
    text = request.values.get("text")

    if text == "":
        response  = "CON What would you want to check \n"
        response += "1. My Account \n"
        response += "2. My phone number"

    elif text == "1":
        response = "END Account number"
    elif text == "2":
        response = "END Phone number"

    view = make_response(response)
    view.headers["Content-type"] = "text/plain"
    return view

if __name__ == "__main__":
    app.run(port=6060, debug=True)