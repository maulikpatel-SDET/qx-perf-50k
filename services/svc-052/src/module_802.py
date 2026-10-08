"""Service module 802: business logic, no crypto."""


def calculate_total_802(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_802():
    return 'module 802 handles orders and invoices'
