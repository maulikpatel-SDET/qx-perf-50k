"""Service module 10937: business logic, no crypto."""


def calculate_total_10937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10937():
    return 'module 10937 handles orders and invoices'
