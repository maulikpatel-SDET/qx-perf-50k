"""Service module 32937: business logic, no crypto."""


def calculate_total_32937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32937():
    return 'module 32937 handles orders and invoices'
