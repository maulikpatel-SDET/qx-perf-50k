"""Service module 37053: business logic, no crypto."""


def calculate_total_37053(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37053():
    return 'module 37053 handles orders and invoices'
