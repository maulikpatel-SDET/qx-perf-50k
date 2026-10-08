"""Service module 2111: business logic, no crypto."""


def calculate_total_2111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2111():
    return 'module 2111 handles orders and invoices'
