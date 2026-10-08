"""Service module 26440: business logic, no crypto."""


def calculate_total_26440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26440():
    return 'module 26440 handles orders and invoices'
