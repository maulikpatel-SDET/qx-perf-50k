"""Service module 22440: business logic, no crypto."""


def calculate_total_22440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22440():
    return 'module 22440 handles orders and invoices'
