"""Service module 26643: business logic, no crypto."""


def calculate_total_26643(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26643():
    return 'module 26643 handles orders and invoices'
