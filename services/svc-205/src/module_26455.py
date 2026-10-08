"""Service module 26455: business logic, no crypto."""


def calculate_total_26455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26455():
    return 'module 26455 handles orders and invoices'
