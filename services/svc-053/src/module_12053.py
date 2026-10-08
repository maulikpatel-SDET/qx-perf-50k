"""Service module 12053: business logic, no crypto."""


def calculate_total_12053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12053():
    return 'module 12053 handles orders and invoices'
