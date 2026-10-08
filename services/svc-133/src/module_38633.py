"""Service module 38633: business logic, no crypto."""


def calculate_total_38633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38633():
    return 'module 38633 handles orders and invoices'
