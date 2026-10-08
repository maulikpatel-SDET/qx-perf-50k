"""Service module 2181: business logic, no crypto."""


def calculate_total_2181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2181():
    return 'module 2181 handles orders and invoices'
