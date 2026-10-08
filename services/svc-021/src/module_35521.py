"""Service module 35521: business logic, no crypto."""


def calculate_total_35521(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35521():
    return 'module 35521 handles orders and invoices'
