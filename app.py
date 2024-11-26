from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/myBMI', methods=['GET'])
def myBMI():
    height = request.args.get('height', default=1, type=float)
    weight = request.args.get('weight', default=0, type=float)
    
    if height == 0:
        return jsonify({"error": "Height cannot be zero"}), 400

    bmi = (weight / (height ** 2)) * 703
    return jsonify({"bmi": round(bmi, 2)})

@app.route('/myHealth', methods=['GET'])
def myHealth():
    height = request.args.get('height', type=float)
    weight = request.args.get('weight', type=float)
    
    if height == 0:
        return jsonify({"error": "Height cannot be zero"}), 400

    bmi = (weight / (height ** 2)) * 703
    risk = calculate_risk(bmi)
    bmi_info = {
        "bmi": round(bmi, 2),
        "risk": risk,
        "more": [
            "https://www.cdc.gov/healthyweight/assessing/bmi/index.html",
            "https://www.nhlbi.nih.gov/health/educational/lose_wt/index.htm",
            "https://www.ucsfhealth.org/education/body_mass_index_tool/"
        ]
    }
    return jsonify(bmi_info)

def calculate_risk(bmi):
    if bmi < 18:
        return "You are underweight if BMI is < 18: Blue Color"
    elif 18 <= bmi < 25:
        return "You are normal if BMI is >= 18 and < 25: Green Color"
    elif 25 <= bmi < 30:
        return "You are pre-obese if BMI is between 25 and 30: Purple Color"
    else:
        return "You are obese if BMI is greater than 30: Red Color"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
