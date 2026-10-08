"""Service module 20862: business logic, no crypto."""


def calculate_total_20862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20862():
    return 'module 20862 handles orders and invoices'
