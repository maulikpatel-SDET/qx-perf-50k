"""Service module 31714: business logic, no crypto."""


def calculate_total_31714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31714():
    return 'module 31714 handles orders and invoices'
