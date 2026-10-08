"""Service module 2281: business logic, no crypto."""


def calculate_total_2281(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2281():
    return 'module 2281 handles orders and invoices'
