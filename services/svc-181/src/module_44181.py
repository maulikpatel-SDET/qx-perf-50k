"""Service module 44181: business logic, no crypto."""


def calculate_total_44181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44181():
    return 'module 44181 handles orders and invoices'
