"""Service module 13161: business logic, no crypto."""


def calculate_total_13161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13161():
    return 'module 13161 handles orders and invoices'
