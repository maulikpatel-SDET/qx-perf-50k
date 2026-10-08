"""Service module 2643: business logic, no crypto."""


def calculate_total_2643(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2643():
    return 'module 2643 handles orders and invoices'
