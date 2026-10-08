"""Service module 11298: business logic, no crypto."""


def calculate_total_11298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11298():
    return 'module 11298 handles orders and invoices'
