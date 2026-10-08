"""Service module 4206: business logic, no crypto."""


def calculate_total_4206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4206():
    return 'module 4206 handles orders and invoices'
