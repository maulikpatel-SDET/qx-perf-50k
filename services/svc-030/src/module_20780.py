"""Service module 20780: business logic, no crypto."""


def calculate_total_20780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20780():
    return 'module 20780 handles orders and invoices'
