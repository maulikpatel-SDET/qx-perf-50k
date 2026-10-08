"""Service module 40732: business logic, no crypto."""


def calculate_total_40732(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40732():
    return 'module 40732 handles orders and invoices'
