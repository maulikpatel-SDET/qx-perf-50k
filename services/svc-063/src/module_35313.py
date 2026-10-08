"""Service module 35313: business logic, no crypto."""


def calculate_total_35313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35313():
    return 'module 35313 handles orders and invoices'
