def analyze_health_data(health_values, threshold):
    if not health_values:
        return "No health data available"

    risk_count = 0
    total_value = 0

    for value in health_values:
        if value < 0 or value > 200:
            continue
        total_value += value

        if value > threshold:
            risk_count += 1

    average_value = total_value / len(health_values)

    if risk_count >=3:
        return "High Risk"
    elif average_value > threshold:
        return "Medium Risk"
    else:
        return "Low Risk"
