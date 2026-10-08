"""Service module 11862: business logic, no crypto."""


def calculate_total_11862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11862():
    return 'module 11862 handles orders and invoices'
