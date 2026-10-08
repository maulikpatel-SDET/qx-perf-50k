"""Service module 44130: business logic, no crypto."""


def calculate_total_44130(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44130():
    return 'module 44130 handles orders and invoices'
