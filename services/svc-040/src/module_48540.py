"""Service module 48540: business logic, no crypto."""


def calculate_total_48540(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48540():
    return 'module 48540 handles orders and invoices'
