"""Service module 15298: business logic, no crypto."""


def calculate_total_15298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15298():
    return 'module 15298 handles orders and invoices'
