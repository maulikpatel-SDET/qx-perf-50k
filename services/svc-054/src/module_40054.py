"""Service module 40054: business logic, no crypto."""


def calculate_total_40054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40054():
    return 'module 40054 handles orders and invoices'
