"""Service module 6005: business logic, no crypto."""


def calculate_total_6005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6005():
    return 'module 6005 handles orders and invoices'
