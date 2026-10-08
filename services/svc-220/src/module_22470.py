"""Service module 22470: business logic, no crypto."""


def calculate_total_22470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22470():
    return 'module 22470 handles orders and invoices'
