"""Service module 20313: business logic, no crypto."""


def calculate_total_20313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20313():
    return 'module 20313 handles orders and invoices'
