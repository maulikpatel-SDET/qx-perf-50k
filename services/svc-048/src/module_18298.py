"""Service module 18298: business logic, no crypto."""


def calculate_total_18298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18298():
    return 'module 18298 handles orders and invoices'
