"""Service module 11226: business logic, no crypto."""


def calculate_total_11226(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11226():
    return 'module 11226 handles orders and invoices'
