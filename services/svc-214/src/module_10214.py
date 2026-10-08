"""Service module 10214: business logic, no crypto."""


def calculate_total_10214(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10214():
    return 'module 10214 handles orders and invoices'
