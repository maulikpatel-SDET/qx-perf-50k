"""Service module 32130: business logic, no crypto."""


def calculate_total_32130(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32130():
    return 'module 32130 handles orders and invoices'
