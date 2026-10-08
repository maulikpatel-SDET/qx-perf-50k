"""Service module 6093: business logic, no crypto."""


def calculate_total_6093(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6093():
    return 'module 6093 handles orders and invoices'
