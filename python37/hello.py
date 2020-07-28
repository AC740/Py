
class Event:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city


def main():
    events = [
        Event("Phantom of the Opera", "New York"),
        Event("Metallica", "Los Angeles"),
        Event("Metallica", "New York"),
        Event("Metallica", "Boston"),
        Event("LadyGaGa", "New York"),
        Event("LadyGaGa", "Boston"),
        Event("LadyGaGa", "Chicago"),
        Event("LadyGaGa", "San Francisco"),
        Event("LadyGaGa", "Washington"),
    ]

    customer = Customer("John", "New York")
    


    # add_to_email(customer, event)
    # 1. Send John an email about all the events in his city
    # for e in events:
    #     if e.city == customer.city:
    #         add_to_email(customer, e)

    
    # [x.city for x in events if city == customer.city]:
     

    for name in [x.name for x in events if x.city == customer.city]:
        print(name)









# YOU DON'T NEED TO UNDERSTAND HOW THESE METHODS WORK
def add_to_email(customer, event, effective_cost = 0):
    distance = get_distance(customer.city, event.city)
    price = get_price(event) if effective_cost == 0 else effective_cost
    miles_away_string = (f" ({distance} miles away)", "")[distance <= 0]
    print(f"{customer.name}: {event.name} in {event.city}{miles_away_string} for ${price}")


def get_price(event):
    return (get_distance(event.city, "") + get_distance(event.name, "")) // 10


def get_distance(from_city, to_city):
    result = 0
    i = 0
    while i < min(len(from_city), len(to_city)):
        result += abs(ord(from_city[i]) - ord(to_city[i]))
        i += 1

    while i < max(len(from_city), len(to_city)):
        result += ord(from_city[i]) if len(from_city) > len(to_city) else ord(to_city[i])
        i += 1
    
    return result

if __name__ == "__main__":
    main()

