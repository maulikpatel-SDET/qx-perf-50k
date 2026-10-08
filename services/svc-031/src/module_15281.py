"""Service module 15281: business logic, no crypto."""


def calculate_total_15281(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15281():
    return 'module 15281 handles orders and invoices'
