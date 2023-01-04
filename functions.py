# encoding=<utf-8>
def calculate_loss_calory(TimeInHours, WeightInKg, SpeedInKmH):
    """function to calculate estimated calorie loss in walking trips 

    Args:
        TimeInHours (int): time of journey
        WeightInKg (int: weight of person
        SpeedInKmH (int): speed of execution in the journey

    Returns:
        string: calories lost
    """
    formula = TimeInHours * WeightInKg * SpeedInKmH
    return f'{formula:.2f} Kcal'

def basal_energy_expenditure(WeightInKg, Height, Age, Sex='male'):
    """Formula of Mifflin-St Jeo 
    to calculate resting energy expenditure for day
    estimate to loss weight

    Args:
        WeightInKg (int): weight of person
        Height (int): height of person
        Age (int): age of person
        Sex (str, optional): 'male' or 'female'. Defaults to 'male'.

    Returns:
        string: resting energy expenditure
    """
    female = (10 * WeightInKg) + (6.25 * Height) - (5.0 * Age) - 161
    male = (10 * WeightInKg) + (6.25 * Height) - (5.0 * Age) + 5
    return f'{male}' if Sex == 'male' else f'{female}'


if __name__ == '__main__':
    print(calculate_loss_calory(0.2833322, 104, 4.6))
    print(basal_energy_expenditure(104, 1.78, 35, 'male'))
