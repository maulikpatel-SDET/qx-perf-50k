"""Service module 13862: business logic, no crypto."""


def calculate_total_13862(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13862():
    return 'module 13862 handles orders and invoices'
