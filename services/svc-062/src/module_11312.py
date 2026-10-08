"""Service module 11312: business logic, no crypto."""


def calculate_total_11312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11312():
    return 'module 11312 handles orders and invoices'
