"""Service module 21181: business logic, no crypto."""


def calculate_total_21181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21181():
    return 'module 21181 handles orders and invoices'
