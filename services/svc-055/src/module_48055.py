"""Service module 48055: business logic, no crypto."""


def calculate_total_48055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48055():
    return 'module 48055 handles orders and invoices'
