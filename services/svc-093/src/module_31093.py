"""Service module 31093: business logic, no crypto."""


def calculate_total_31093(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31093():
    return 'module 31093 handles orders and invoices'
