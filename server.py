from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # or your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your@email.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your@email.com'

mail = Mail(app)

@app.route('/submit-referral', methods=['POST'])
def submit_referral():
    data = request.json

    body = f"""
    New Patient Referral
    --------------------
    Patient Name:              {data.get('patient_first_name')} {data.get('patient_last_name')}
    Date of Birth:             {data.get('date_of_birth')}
    Phone Number:              {data.get('phone_number')}
    Ordering Physician:        {data.get('ordering_physician')}
    Ordering Physician Email:  {data.get('ordering_physician_email')}
    Comments:                  {data.get('comments')}
    """

    try:
        msg = Message(
            subject='New Patient Referral',
            recipients=['admin@SunriseSpine.com'],
            body=body
        )
        mail.send(msg)
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run()