"""Service module 35208: business logic, no crypto."""


def calculate_total_35208(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35208():
    return 'module 35208 handles orders and invoices'
