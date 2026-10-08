"""Service module 16617: business logic, no crypto."""


def calculate_total_16617(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16617():
    return 'module 16617 handles orders and invoices'
