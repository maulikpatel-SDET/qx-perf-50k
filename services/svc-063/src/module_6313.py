"""Service module 6313: business logic, no crypto."""


def calculate_total_6313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6313():
    return 'module 6313 handles orders and invoices'
