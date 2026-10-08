"""Service module 29617: business logic, no crypto."""


def calculate_total_29617(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29617():
    return 'module 29617 handles orders and invoices'
