"""Service module 40181: business logic, no crypto."""


def calculate_total_40181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40181():
    return 'module 40181 handles orders and invoices'
