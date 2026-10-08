"""Service module 23452: business logic, no crypto."""


def calculate_total_23452(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23452():
    return 'module 23452 handles orders and invoices'
