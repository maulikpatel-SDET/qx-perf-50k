"""Service module 32617: business logic, no crypto."""


def calculate_total_32617(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32617():
    return 'module 32617 handles orders and invoices'
