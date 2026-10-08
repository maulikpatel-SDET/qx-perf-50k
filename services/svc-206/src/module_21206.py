"""Service module 21206: business logic, no crypto."""


def calculate_total_21206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21206():
    return 'module 21206 handles orders and invoices'
