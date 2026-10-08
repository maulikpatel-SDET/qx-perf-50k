"""Service module 21093: business logic, no crypto."""


def calculate_total_21093(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21093():
    return 'module 21093 handles orders and invoices'
