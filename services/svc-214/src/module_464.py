"""Service module 464: business logic, no crypto."""


def calculate_total_464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_464():
    return 'module 464 handles orders and invoices'
