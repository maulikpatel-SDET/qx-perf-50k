"""Service module 38617: business logic, no crypto."""


def calculate_total_38617(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38617():
    return 'module 38617 handles orders and invoices'
