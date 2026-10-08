"""Service module 2093: business logic, no crypto."""


def calculate_total_2093(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2093():
    return 'module 2093 handles orders and invoices'
