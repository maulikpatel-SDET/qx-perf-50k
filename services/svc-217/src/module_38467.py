"""Service module 38467: business logic, no crypto."""


def calculate_total_38467(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38467():
    return 'module 38467 handles orders and invoices'
