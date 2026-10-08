"""Service module 35488: business logic, no crypto."""


def calculate_total_35488(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35488():
    return 'module 35488 handles orders and invoices'
