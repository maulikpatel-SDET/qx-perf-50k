"""Service module 14718: business logic, no crypto."""


def calculate_total_14718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14718():
    return 'module 14718 handles orders and invoices'
