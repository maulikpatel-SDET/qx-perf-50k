"""Service module 12714: business logic, no crypto."""


def calculate_total_12714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12714():
    return 'module 12714 handles orders and invoices'
