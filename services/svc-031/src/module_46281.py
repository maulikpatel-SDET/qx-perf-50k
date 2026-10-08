"""Service module 46281: business logic, no crypto."""


def calculate_total_46281(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46281():
    return 'module 46281 handles orders and invoices'
