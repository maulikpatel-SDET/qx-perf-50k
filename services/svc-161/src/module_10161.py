"""Service module 10161: business logic, no crypto."""


def calculate_total_10161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10161():
    return 'module 10161 handles orders and invoices'
