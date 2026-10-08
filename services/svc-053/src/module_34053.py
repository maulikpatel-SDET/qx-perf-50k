"""Service module 34053: business logic, no crypto."""


def calculate_total_34053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34053():
    return 'module 34053 handles orders and invoices'
