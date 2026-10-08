"""Service module 41313: business logic, no crypto."""


def calculate_total_41313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41313():
    return 'module 41313 handles orders and invoices'
