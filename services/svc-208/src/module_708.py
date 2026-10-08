"""Service module 708: business logic, no crypto."""


def calculate_total_708(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_708():
    return 'module 708 handles orders and invoices'
