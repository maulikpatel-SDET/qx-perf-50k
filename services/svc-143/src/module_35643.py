"""Service module 35643: business logic, no crypto."""


def calculate_total_35643(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35643():
    return 'module 35643 handles orders and invoices'
