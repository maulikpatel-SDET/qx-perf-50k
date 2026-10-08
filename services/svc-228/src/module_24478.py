"""Service module 24478: business logic, no crypto."""


def calculate_total_24478(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24478():
    return 'module 24478 handles orders and invoices'
