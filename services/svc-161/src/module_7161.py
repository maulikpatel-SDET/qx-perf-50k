"""Service module 7161: business logic, no crypto."""


def calculate_total_7161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7161():
    return 'module 7161 handles orders and invoices'
