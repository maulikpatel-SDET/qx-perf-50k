"""Service module 13298: business logic, no crypto."""


def calculate_total_13298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13298():
    return 'module 13298 handles orders and invoices'
