"""Service module 1143: business logic, no crypto."""


def calculate_total_1143(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1143():
    return 'module 1143 handles orders and invoices'
