"""Service module 49206: business logic, no crypto."""


def calculate_total_49206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49206():
    return 'module 49206 handles orders and invoices'
