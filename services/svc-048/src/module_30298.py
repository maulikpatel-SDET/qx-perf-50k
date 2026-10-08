"""Service module 30298: business logic, no crypto."""


def calculate_total_30298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30298():
    return 'module 30298 handles orders and invoices'
