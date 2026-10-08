"""Service module 12317: business logic, no crypto."""


def calculate_total_12317(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12317():
    return 'module 12317 handles orders and invoices'
