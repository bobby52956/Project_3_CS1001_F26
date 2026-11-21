from data import CountyDemographics

# Purpose: Calculate the combined 2014 population of all counties provided.
# Inputs: counties, a list of CountyDemographics objects.
# Output: The total 2014 population as an integer.
def population_total(counties: list[CountyDemographics]) -> int:
    sum = 0
    for county in counties:
        sum += county.population["2014 Population"]
    return sum

# Purpose: Create a list containing only counties in the requested state.
# Inputs: counties, a list of CountyDemographics objects; state, a state abbreviation.
# Output: A list of CountyDemographics objects located in that state.
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.state == state:
            result.append(county)
    return result

# Purpose: Estimate the total 2014 population with a specified education category.
# Inputs: counties, a list of CountyDemographics objects; key, an education dictionary key.
# Output: The estimated sub-population as a float, or 0 if the key does not exist.
def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = 0.0
    for county in counties:
        num = county.population["2014 Population"]*(county.education[key]/100)
        total += num
    return total

# Purpose: Estimate the total 2014 population belonging to an ethnicity category.
# Inputs: counties, a list of CountyDemographics objects; key, an ethnicity dictionary key.
# Output: The estimated sub-population as a float.
def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        num = county.population["2014 Population"]*(county.ethnicities[key]/100)
        total += num
    return total

# Purpose: Estimate the total 2014 population below the poverty level.
# Inputs: counties, a list of CountyDemographics objects.
# Output: The estimated population below the poverty level as a float.
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0
    for county in counties:
        num = county.population["2014 Population"]*(county.income['Persons Below Poverty Level']/100)
        total += num
    return total

# Purpose: Calculate the percentage of the supplied population in an education category.
# Inputs: counties, a list of CountyDemographics objects; key, an education dictionary key.
# Output: The education-category percentage as a float, or 0 for an empty list.
def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    if len(counties) == 0:
        return 0
    sub_population = 0
    population = 0
    for county in counties:
        sub_population += population_by_education(counties,key)
        population += population_total(counties)
    return (sub_population/population) *100

# Purpose: Calculate the percentage of the supplied population in an ethnicity category.
# Inputs: counties, a list of CountyDemographics objects; key, an ethnicity dictionary key.
# Output: The ethnicity-category percentage as a float, or 0 for an empty list.
def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    if len(counties) == 0:
        return 0
    sub_population = 0
    population = 0
    for county in counties:
        sub_population += population_by_ethnicity(counties,key)
        population += population_total(counties)
    return (sub_population/population) *100

# Purpose: Calculate the percentage of the supplied population below the poverty level.
# Inputs: counties, a list of CountyDemographics objects.
# Output: The percentage below the poverty level as a float, or 0 for an empty list.
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    if len(counties) == 0:
        return 0
    sub_population = 0
    population = 0
    for county in counties:
        sub_population += population_below_poverty_level(counties)
        population += population_total(counties)
    return (sub_population/population) *100

# Purpose: Find counties whose specified education percentage is greater than a threshold.
# Inputs: counties, a list of CountyDemographics objects; key, an education dictionary key;
#         threshold, the percentage to compare against.
# Output: A list of counties with an education percentage greater than the threshold.
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    greater = []
    for county in counties:
        if county.education[key] > threshold:
            greater.append(county)
    return greater

# Purpose: Find counties whose specified education percentage is less than a threshold.
# Inputs: counties, a list of CountyDemographics objects; key, an education dictionary key;
#         threshold, the percentage to compare against.
# Output: A list of counties with an education percentage less than the threshold.
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    less = []
    for county in counties:
        if county.education[key] < threshold:
            less.append(county)
    return less

# Purpose: Find counties whose specified ethnicity percentage is greater than a threshold.
# Inputs: counties, a list of CountyDemographics objects; key, an ethnicity dictionary key;
#         threshold, the percentage to compare against.
# Output: A list of counties with an ethnicity percentage greater than the threshold.
def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    greater = []
    for county in counties:
        if county.ethnicities[key] > threshold:
            greater.append(county)
    return greater

# Purpose: Find counties whose specified ethnicity percentage is less than a threshold.
# Inputs: counties, a list of CountyDemographics objects; key, an ethnicity dictionary key;
#         threshold, the percentage to compare against.
# Output: A list of counties with an ethnicity percentage less than the threshold.
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    less = []
    for county in counties:
        if county.ethnicities[key] < threshold:
            less.append(county)
    return less

# Purpose: Find counties whose poverty-level percentage is greater than a threshold.
# Inputs: counties, a list of CountyDemographics objects; threshold, a percentage.
# Output: A list of counties with a poverty-level percentage greater than the threshold.
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    greater = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > threshold:
            greater.append(county)
    return greater

# Purpose: Find counties whose poverty-level percentage is less than a threshold.
# Inputs: counties, a list of CountyDemographics objects; threshold, a percentage.
# Output: A list of counties with a poverty-level percentage less than the threshold.
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    less = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            less.append(county)
    return less

