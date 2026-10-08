"""Service module 71: business logic, no crypto."""


def calculate_total_71(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_71():
    return 'module 71 handles orders and invoices'
