"""Service module 38214: business logic, no crypto."""


def calculate_total_38214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38214():
    return 'module 38214 handles orders and invoices'
