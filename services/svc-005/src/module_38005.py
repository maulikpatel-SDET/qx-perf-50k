"""Service module 38005: business logic, no crypto."""


def calculate_total_38005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38005():
    return 'module 38005 handles orders and invoices'
