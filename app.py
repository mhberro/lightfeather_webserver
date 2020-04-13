from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/api/encode', methods=["POST"])
def encode():
	try:
		req_data = request.get_json()
		shift = req_data['Shift']
		message = req_data['Message']
		EncodedMessage = {'EncodedMessage': shift_cipher(shift, message)}

		with open('EncodedMessage.json', 'w') as f:
			json.dump(EncodedMessage, f)

		return EncodedMessage['EncodedMessage'], 200
	except Exception as e:
		return " ", 500

def shift_cipher(shift, message):
	temp = []
	for v in message:
		temp += v if v == " " else chr(((ord(v) - ord(' ') + shift) % 95) + ord(' '))
	return "".join(temp)

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=23456)