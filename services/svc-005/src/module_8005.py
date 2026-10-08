"""Service module 8005: business logic, no crypto."""


def calculate_total_8005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8005():
    return 'module 8005 handles orders and invoices'
