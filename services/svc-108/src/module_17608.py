"""Service module 17608: business logic, no crypto."""


def calculate_total_17608(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17608():
    return 'module 17608 handles orders and invoices'
