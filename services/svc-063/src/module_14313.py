"""Service module 14313: business logic, no crypto."""


def calculate_total_14313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14313():
    return 'module 14313 handles orders and invoices'
