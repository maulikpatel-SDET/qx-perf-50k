"""Service module 16440: business logic, no crypto."""


def calculate_total_16440(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16440():
    return 'module 16440 handles orders and invoices'
