"""Service module 41053: business logic, no crypto."""


def calculate_total_41053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41053():
    return 'module 41053 handles orders and invoices'
