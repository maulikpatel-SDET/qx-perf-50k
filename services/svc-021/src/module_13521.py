"""Service module 13521: business logic, no crypto."""


def calculate_total_13521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13521():
    return 'module 13521 handles orders and invoices'
