"""Service module 28053: business logic, no crypto."""


def calculate_total_28053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28053():
    return 'module 28053 handles orders and invoices'
