"""Service module 158: business logic, no crypto."""


def calculate_total_158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_158():
    return 'module 158 handles orders and invoices'
