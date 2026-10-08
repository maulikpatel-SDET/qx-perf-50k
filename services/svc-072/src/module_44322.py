"""Service module 44322: business logic, no crypto."""


def calculate_total_44322(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44322():
    return 'module 44322 handles orders and invoices'
