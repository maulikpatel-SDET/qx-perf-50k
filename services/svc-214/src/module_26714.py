"""Service module 26714: business logic, no crypto."""


def calculate_total_26714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26714():
    return 'module 26714 handles orders and invoices'
