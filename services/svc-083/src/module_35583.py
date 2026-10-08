"""Service module 35583: business logic, no crypto."""


def calculate_total_35583(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35583():
    return 'module 35583 handles orders and invoices'
