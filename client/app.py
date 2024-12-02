from flask import Flask, render_template, request
import requests

app = Flask(__name__)

my_health_url = "https://34.8.81.248.nip.io/bmi/myHealth"

class BMI:
    def __init__(self, bmi=0, risk="", more=None):
        if more is None:
            more = [
                "https://www.cdc.gov/healthyweight/assessing/bmi/index.html",
                "https://www.nhlbi.nih.gov/health/educational/lose_wt/index.htm",
                "https://www.ucsfhealth.org/education/body_mass_index_tool/"
            ]
        self.bmi = bmi
        self.risk = risk
        self.more = more

@app.route('/', methods=['GET', 'POST'])
def index():
    output_message = ""
    color = "black"

    if request.method == 'POST':
        height = request.form.get('height', type=float)
        weight = request.form.get('weight', type=float)

        if height > 0 and weight > 0:
            # Call the myHealth service using REST
            health_response = requests.get(f"{my_health_url}?height={height}&weight={weight}")
            
            if health_response.status_code == 200:
                health_details = health_response.json()
                output_message = f"Your calculated health status: {health_details['risk']}"
                color = "black"  # Set color based on your logic
            else:
                output_message = "Error retrieving health information."
                color = "red"
        else:
            output_message = "Height and weight must be greater than 0."
            color = "red"

    return render_template('index.html', output_message=output_message, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)