"""Service module 36559: business logic, no crypto."""


def calculate_total_36559(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36559():
    return 'module 36559 handles orders and invoices'
