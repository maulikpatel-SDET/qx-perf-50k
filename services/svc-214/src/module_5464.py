"""Service module 5464: business logic, no crypto."""


def calculate_total_5464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5464():
    return 'module 5464 handles orders and invoices'
