"""Service module 36313: business logic, no crypto."""


def calculate_total_36313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36313():
    return 'module 36313 handles orders and invoices'
