"""Service module 49384: business logic, no crypto."""


def calculate_total_49384(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49384():
    return 'module 49384 handles orders and invoices'
