distance_mi = 1
is_raining = True
has_bike = False
has_car = False
has_ride_share_app = True

if not distance_mi or not isinstance(distance_mi, (int, float)):
    print(False)

elif distance_mi <= 1 and not is_raining:
    print(True)
elif distance_mi <= 1 and is_raining:
    print(False)

elif 1 <= distance_mi <= 6 and (is_raining and not has_bike):
    print(False)
elif 1 <= distance_mi <= 6 and (not is_raining and not has_bike):
    print(False)
elif 1 <= distance_mi <= 6 and (not is_raining and has_bike):
    print(True)
    
elif distance_mi > 6 and has_ride_share_app:
    print(True)
elif distance_mi > 6 and has_car:
    print(True)
elif distance_mi > 6 and (not has_car and not has_ride_share_app):
    print(False)

