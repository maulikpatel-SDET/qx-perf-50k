"""Service module 6862: business logic, no crypto."""


def calculate_total_6862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6862():
    return 'module 6862 handles orders and invoices'
