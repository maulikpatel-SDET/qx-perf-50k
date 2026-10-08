"""Service module 40281: business logic, no crypto."""


def calculate_total_40281(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40281():
    return 'module 40281 handles orders and invoices'
