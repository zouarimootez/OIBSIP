def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_bmi_recommendation(category):
    """Provide health recommendations based on BMI category."""
    recommendations = {
        "Underweight": "Consider gaining weight through a balanced diet and exercise.",
        "Normal weight": "Maintain your current weight with a healthy lifestyle.",
        "Overweight": "Consider losing weight through diet and exercise.",
        "Obese": "Seek medical advice for weight management."
    }
    return recommendations.get(category, "No recommendation available.")