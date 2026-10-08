"""Service module 21313: business logic, no crypto."""


def calculate_total_21313(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21313():
    return 'module 21313 handles orders and invoices'
