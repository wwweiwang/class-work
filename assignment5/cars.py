# 8-12
def build_profile(manufacturer, model, **car_info):

    profile = {}
    profile['manufacturer_name'] = manufacturer
    profile['model_name'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_profile = build_profile('VW', 'GTI',
                                color='black',
                                year='2015')
print(car_profile)
