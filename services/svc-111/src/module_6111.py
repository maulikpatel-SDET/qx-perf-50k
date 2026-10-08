"""Service module 6111: business logic, no crypto."""


def calculate_total_6111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6111():
    return 'module 6111 handles orders and invoices'
