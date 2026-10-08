"""Service module 30181: business logic, no crypto."""


def calculate_total_30181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30181():
    return 'module 30181 handles orders and invoices'
