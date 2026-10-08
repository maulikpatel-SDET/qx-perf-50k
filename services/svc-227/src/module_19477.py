"""Service module 19477: business logic, no crypto."""


def calculate_total_19477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19477():
    return 'module 19477 handles orders and invoices'
