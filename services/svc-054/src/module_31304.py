"""Service module 31304: business logic, no crypto."""


def calculate_total_31304(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31304():
    return 'module 31304 handles orders and invoices'
