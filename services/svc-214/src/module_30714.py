"""Service module 30714: business logic, no crypto."""


def calculate_total_30714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30714():
    return 'module 30714 handles orders and invoices'
