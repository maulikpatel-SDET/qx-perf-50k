"""Service module 38862: business logic, no crypto."""


def calculate_total_38862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38862():
    return 'module 38862 handles orders and invoices'
