"""Service module 35862: business logic, no crypto."""


def calculate_total_35862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35862():
    return 'module 35862 handles orders and invoices'
