"""Service module 3633: business logic, no crypto."""


def calculate_total_3633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3633():
    return 'module 3633 handles orders and invoices'
