"""Service module 7111: business logic, no crypto."""


def calculate_total_7111(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7111():
    return 'module 7111 handles orders and invoices'
