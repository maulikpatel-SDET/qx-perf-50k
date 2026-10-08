"""Service module 23896: business logic, no crypto."""


def calculate_total_23896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23896():
    return 'module 23896 handles orders and invoices'
