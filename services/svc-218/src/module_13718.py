"""Service module 13718: business logic, no crypto."""


def calculate_total_13718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13718():
    return 'module 13718 handles orders and invoices'
