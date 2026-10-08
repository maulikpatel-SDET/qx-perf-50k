"""Service module 26111: business logic, no crypto."""


def calculate_total_26111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26111():
    return 'module 26111 handles orders and invoices'
