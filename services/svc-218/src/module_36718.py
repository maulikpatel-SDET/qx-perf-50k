"""Service module 36718: business logic, no crypto."""


def calculate_total_36718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36718():
    return 'module 36718 handles orders and invoices'
