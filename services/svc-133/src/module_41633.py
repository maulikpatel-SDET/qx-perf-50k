"""Service module 41633: business logic, no crypto."""


def calculate_total_41633(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41633():
    return 'module 41633 handles orders and invoices'
