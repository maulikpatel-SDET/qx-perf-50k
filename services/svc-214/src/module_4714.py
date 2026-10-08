"""Service module 4714: business logic, no crypto."""


def calculate_total_4714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4714():
    return 'module 4714 handles orders and invoices'
