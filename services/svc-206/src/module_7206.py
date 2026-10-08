"""Service module 7206: business logic, no crypto."""


def calculate_total_7206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7206():
    return 'module 7206 handles orders and invoices'
