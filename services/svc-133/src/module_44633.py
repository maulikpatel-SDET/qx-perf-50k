"""Service module 44633: business logic, no crypto."""


def calculate_total_44633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44633():
    return 'module 44633 handles orders and invoices'
