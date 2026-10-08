"""Service module 41488: business logic, no crypto."""


def calculate_total_41488(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41488():
    return 'module 41488 handles orders and invoices'
