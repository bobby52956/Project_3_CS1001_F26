from data import CountyDemographics

def population_total(counties: list[CountyDemographics]) -> int:
    sum = 0
    for county in counties:
        sum += county.population["2014 Population"]
    return sum

def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    result = []
    for county in counties:
        if county.state == state:
            result.append(county)
    return result

def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        num = county.population["2014 Population"]*(county.education[key]/100)
        total += num
    return total

def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = 0
    for county in counties:
        num = county.population["2014 Population"]*(county.ethnicities[key]/100)
        total += num
    return total

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0
    for county in counties:
        num = county.population["2014 Population"]*(county.income['Persons Below Poverty Level']/100)
        total += num
    return total

def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    if len(counties) == 0:
        return 0
    sub_population = 0
    population = 0
    for county in counties:
        sub_population += population_by_education(counties,key)
        population += population_total(counties)
    return (sub_population/population) *100

def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    if len(counties) == 0:
        return 0
    sub_population = 0
    population = 0
    for county in counties:
        sub_population += population_by_ethnicity(counties,key)
        population += population_total(counties)
    return (sub_population/population) *100

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    if len(counties) == 0:
        return 0
    sub_population = 0
    population = 0
    for county in counties:
        sub_population += population_below_poverty_level(counties)
        population += population_total(counties)
    return (sub_population/population) *100

def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    greater = []
    for county in counties:
        if county.education[key] > threshold:
            greater.append(county)
    return greater

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    less = []
    for county in counties:
        if county.education[key] < threshold:
            less.append(county)
    return less

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    greater = []
    for county in counties:
        if county.ethnicities[key] > threshold:
            greater.append(county)
    return greater

def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    less = []
    for county in counties:
        if county.ethnicities[key] < threshold:
            less.append(county)
    return less

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    greater = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > threshold:
            greater.append(county)
    return greater

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    less = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            less.append(county)
    return less

