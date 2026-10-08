"""Service module 31937: business logic, no crypto."""


def calculate_total_31937(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31937():
    return 'module 31937 handles orders and invoices'
