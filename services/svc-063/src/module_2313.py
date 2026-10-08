"""Service module 2313: business logic, no crypto."""


def calculate_total_2313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2313():
    return 'module 2313 handles orders and invoices'
