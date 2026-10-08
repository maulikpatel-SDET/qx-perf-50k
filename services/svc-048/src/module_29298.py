"""Service module 29298: business logic, no crypto."""


def calculate_total_29298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29298():
    return 'module 29298 handles orders and invoices'
