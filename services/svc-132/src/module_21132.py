"""Service module 21132: business logic, no crypto."""


def calculate_total_21132(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21132():
    return 'module 21132 handles orders and invoices'
