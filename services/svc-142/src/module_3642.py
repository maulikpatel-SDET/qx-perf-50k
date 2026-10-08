"""Service module 3642: business logic, no crypto."""


def calculate_total_3642(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3642():
    return 'module 3642 handles orders and invoices'
