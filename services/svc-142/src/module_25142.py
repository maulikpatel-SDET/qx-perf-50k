"""Service module 25142: business logic, no crypto."""


def calculate_total_25142(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25142():
    return 'module 25142 handles orders and invoices'
