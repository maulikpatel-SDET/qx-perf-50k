"""Service module 5708: business logic, no crypto."""


def calculate_total_5708(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5708():
    return 'module 5708 handles orders and invoices'
