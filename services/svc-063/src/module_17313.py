"""Service module 17313: business logic, no crypto."""


def calculate_total_17313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17313():
    return 'module 17313 handles orders and invoices'
