"""Service module 34313: business logic, no crypto."""


def calculate_total_34313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34313():
    return 'module 34313 handles orders and invoices'
