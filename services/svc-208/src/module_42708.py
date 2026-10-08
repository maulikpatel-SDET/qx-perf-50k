"""Service module 42708: business logic, no crypto."""


def calculate_total_42708(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42708():
    return 'module 42708 handles orders and invoices'
