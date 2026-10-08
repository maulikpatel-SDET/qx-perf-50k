"""Service module 28600: business logic, no crypto."""


def calculate_total_28600(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28600():
    return 'module 28600 handles orders and invoices'
