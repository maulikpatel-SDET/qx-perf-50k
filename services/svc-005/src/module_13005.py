"""Service module 13005: business logic, no crypto."""


def calculate_total_13005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13005():
    return 'module 13005 handles orders and invoices'
