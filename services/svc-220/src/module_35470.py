"""Service module 35470: business logic, no crypto."""


def calculate_total_35470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35470():
    return 'module 35470 handles orders and invoices'
