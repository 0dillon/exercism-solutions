def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and int(temperature * neutrons_emitted) < 500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power)*100
    if efficiency >= 80:
        return "green"
    elif efficiency >= 60:
        return "orange"
    elif efficiency >= 30:
        return "red"
    return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    status_code = "DANGER"
    criticality = temperature * neutrons_produced_per_second
    if criticality < (threshold * 0.9):
        status_code = "LOW"
    elif (threshold * 0.9) <= criticality <= (threshold * 1.1):
        status_code = "NORMAL"
    return status_code









    
