"""Service module 5451: business logic, no crypto."""


def calculate_total_5451(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5451():
    return 'module 5451 handles orders and invoices'
