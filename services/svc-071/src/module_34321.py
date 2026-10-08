"""Service module 34321: business logic, no crypto."""


def calculate_total_34321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34321():
    return 'module 34321 handles orders and invoices'
