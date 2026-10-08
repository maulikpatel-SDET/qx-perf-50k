"""Service module 42111: business logic, no crypto."""


def calculate_total_42111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42111():
    return 'module 42111 handles orders and invoices'
