"""Service module 12224: business logic, no crypto."""


def calculate_total_12224(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12224():
    return 'module 12224 handles orders and invoices'
