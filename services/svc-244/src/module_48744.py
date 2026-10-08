"""Service module 48744: business logic, no crypto."""


def calculate_total_48744(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48744():
    return 'module 48744 handles orders and invoices'
