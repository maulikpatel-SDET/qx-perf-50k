"""Service module 34005: business logic, no crypto."""


def calculate_total_34005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34005():
    return 'module 34005 handles orders and invoices'
