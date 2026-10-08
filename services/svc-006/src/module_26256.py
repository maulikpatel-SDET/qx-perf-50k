"""Service module 26256: business logic, no crypto."""


def calculate_total_26256(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26256():
    return 'module 26256 handles orders and invoices'
