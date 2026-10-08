"""Service module 32298: business logic, no crypto."""


def calculate_total_32298(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32298():
    return 'module 32298 handles orders and invoices'
