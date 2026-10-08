"""Service module 19005: business logic, no crypto."""


def calculate_total_19005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19005():
    return 'module 19005 handles orders and invoices'
