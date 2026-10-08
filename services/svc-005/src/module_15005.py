"""Service module 15005: business logic, no crypto."""


def calculate_total_15005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15005():
    return 'module 15005 handles orders and invoices'
