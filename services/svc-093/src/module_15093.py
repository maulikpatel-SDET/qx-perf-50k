"""Service module 15093: business logic, no crypto."""


def calculate_total_15093(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15093():
    return 'module 15093 handles orders and invoices'
