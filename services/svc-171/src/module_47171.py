"""Service module 47171: business logic, no crypto."""


def calculate_total_47171(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47171():
    return 'module 47171 handles orders and invoices'
