"""Service module 33862: business logic, no crypto."""


def calculate_total_33862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33862():
    return 'module 33862 handles orders and invoices'
