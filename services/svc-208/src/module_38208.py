"""Service module 38208: business logic, no crypto."""


def calculate_total_38208(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38208():
    return 'module 38208 handles orders and invoices'
