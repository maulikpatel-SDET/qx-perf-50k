"""Service module 8583: business logic, no crypto."""


def calculate_total_8583(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8583():
    return 'module 8583 handles orders and invoices'
