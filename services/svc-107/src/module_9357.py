"""Service module 9357: business logic, no crypto."""


def calculate_total_9357(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9357():
    return 'module 9357 handles orders and invoices'
