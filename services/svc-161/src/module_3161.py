"""Service module 3161: business logic, no crypto."""


def calculate_total_3161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3161():
    return 'module 3161 handles orders and invoices'
