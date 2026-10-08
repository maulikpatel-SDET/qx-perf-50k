"""Service module 26161: business logic, no crypto."""


def calculate_total_26161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26161():
    return 'module 26161 handles orders and invoices'
