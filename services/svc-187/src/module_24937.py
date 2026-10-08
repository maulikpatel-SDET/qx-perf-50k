"""Service module 24937: business logic, no crypto."""


def calculate_total_24937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24937():
    return 'module 24937 handles orders and invoices'
