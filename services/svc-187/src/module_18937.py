"""Service module 18937: business logic, no crypto."""


def calculate_total_18937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18937():
    return 'module 18937 handles orders and invoices'
