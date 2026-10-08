"""Service module 9206: business logic, no crypto."""


def calculate_total_9206(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9206():
    return 'module 9206 handles orders and invoices'
