"""Service module 13143: business logic, no crypto."""


def calculate_total_13143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13143():
    return 'module 13143 handles orders and invoices'
