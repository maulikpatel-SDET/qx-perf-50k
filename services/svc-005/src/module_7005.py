"""Service module 7005: business logic, no crypto."""


def calculate_total_7005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7005():
    return 'module 7005 handles orders and invoices'
