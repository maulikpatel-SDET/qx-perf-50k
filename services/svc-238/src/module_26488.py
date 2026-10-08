"""Service module 26488: business logic, no crypto."""


def calculate_total_26488(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26488():
    return 'module 26488 handles orders and invoices'
