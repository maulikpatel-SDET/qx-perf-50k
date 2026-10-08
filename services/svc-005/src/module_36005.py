"""Service module 36005: business logic, no crypto."""


def calculate_total_36005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36005():
    return 'module 36005 handles orders and invoices'
