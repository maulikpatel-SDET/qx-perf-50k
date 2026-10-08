"""Service module 12313: business logic, no crypto."""


def calculate_total_12313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12313():
    return 'module 12313 handles orders and invoices'
