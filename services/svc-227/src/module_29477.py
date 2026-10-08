"""Service module 29477: business logic, no crypto."""


def calculate_total_29477(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29477():
    return 'module 29477 handles orders and invoices'
