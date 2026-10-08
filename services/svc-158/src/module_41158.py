"""Service module 41158: business logic, no crypto."""


def calculate_total_41158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41158():
    return 'module 41158 handles orders and invoices'
