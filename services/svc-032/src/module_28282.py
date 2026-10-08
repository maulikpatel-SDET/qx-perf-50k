"""Service module 28282: business logic, no crypto."""


def calculate_total_28282(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28282():
    return 'module 28282 handles orders and invoices'
