"""Service module 42633: business logic, no crypto."""


def calculate_total_42633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42633():
    return 'module 42633 handles orders and invoices'
