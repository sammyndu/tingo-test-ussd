from flask import Flask, request, Response

app = Flask(__name__)

response = "yes"

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

    ##Response(headers={"Content-type": "text/plain"})
    return response

if __name__ == "__main__":
    app.run(debug=True)