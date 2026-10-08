"""Service module 41293: business logic, no crypto."""


def calculate_total_41293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41293():
    return 'module 41293 handles orders and invoices'
