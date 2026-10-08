"""Service module 17714: business logic, no crypto."""


def calculate_total_17714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17714():
    return 'module 17714 handles orders and invoices'
