"""Service module 13226: business logic, no crypto."""


def calculate_total_13226(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13226():
    return 'module 13226 handles orders and invoices'
