"""Service module 41298: business logic, no crypto."""


def calculate_total_41298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41298():
    return 'module 41298 handles orders and invoices'
