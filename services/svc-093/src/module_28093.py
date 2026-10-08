"""Service module 28093: business logic, no crypto."""


def calculate_total_28093(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28093():
    return 'module 28093 handles orders and invoices'
