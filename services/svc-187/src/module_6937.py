"""Service module 6937: business logic, no crypto."""


def calculate_total_6937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6937():
    return 'module 6937 handles orders and invoices'
