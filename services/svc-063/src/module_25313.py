"""Service module 25313: business logic, no crypto."""


def calculate_total_25313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25313():
    return 'module 25313 handles orders and invoices'
