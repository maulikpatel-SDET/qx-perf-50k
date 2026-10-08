"""Service module 26181: business logic, no crypto."""


def calculate_total_26181(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26181():
    return 'module 26181 handles orders and invoices'
