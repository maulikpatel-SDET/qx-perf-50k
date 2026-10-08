"""Service module 17005: business logic, no crypto."""


def calculate_total_17005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17005():
    return 'module 17005 handles orders and invoices'
