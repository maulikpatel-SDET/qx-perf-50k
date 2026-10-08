"""Service module 41161: business logic, no crypto."""


def calculate_total_41161(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41161():
    return 'module 41161 handles orders and invoices'
