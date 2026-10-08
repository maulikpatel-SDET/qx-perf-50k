"""Service module 35130: business logic, no crypto."""


def calculate_total_35130(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35130():
    return 'module 35130 handles orders and invoices'
