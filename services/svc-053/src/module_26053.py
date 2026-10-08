"""Service module 26053: business logic, no crypto."""


def calculate_total_26053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26053():
    return 'module 26053 handles orders and invoices'
