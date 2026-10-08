"""Service module 16005: business logic, no crypto."""


def calculate_total_16005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16005():
    return 'module 16005 handles orders and invoices'
