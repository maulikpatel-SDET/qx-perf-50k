"""Service module 48298: business logic, no crypto."""


def calculate_total_48298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48298():
    return 'module 48298 handles orders and invoices'
