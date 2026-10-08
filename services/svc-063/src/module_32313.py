"""Service module 32313: business logic, no crypto."""


def calculate_total_32313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32313():
    return 'module 32313 handles orders and invoices'
