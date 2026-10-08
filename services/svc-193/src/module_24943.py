"""Service module 24943: business logic, no crypto."""


def calculate_total_24943(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24943():
    return 'module 24943 handles orders and invoices'
