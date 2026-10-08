"""Service module 14212: business logic, no crypto."""


def calculate_total_14212(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14212():
    return 'module 14212 handles orders and invoices'
