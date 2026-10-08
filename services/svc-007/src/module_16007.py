"""Service module 16007: business logic, no crypto."""


def calculate_total_16007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16007():
    return 'module 16007 handles orders and invoices'
