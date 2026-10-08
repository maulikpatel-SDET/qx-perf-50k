"""Service module 30143: business logic, no crypto."""


def calculate_total_30143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30143():
    return 'module 30143 handles orders and invoices'
