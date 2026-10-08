"""Service module 19943: business logic, no crypto."""


def calculate_total_19943(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19943():
    return 'module 19943 handles orders and invoices'
