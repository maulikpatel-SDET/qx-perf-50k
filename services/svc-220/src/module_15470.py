"""Service module 15470: business logic, no crypto."""


def calculate_total_15470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15470():
    return 'module 15470 handles orders and invoices'
