"""Service module 30718: business logic, no crypto."""


def calculate_total_30718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30718():
    return 'module 30718 handles orders and invoices'
