"""Service module 21718: business logic, no crypto."""


def calculate_total_21718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21718():
    return 'module 21718 handles orders and invoices'
