"""Service module 33161: business logic, no crypto."""


def calculate_total_33161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33161():
    return 'module 33161 handles orders and invoices'
