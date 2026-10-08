"""Service module 41005: business logic, no crypto."""


def calculate_total_41005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41005():
    return 'module 41005 handles orders and invoices'
