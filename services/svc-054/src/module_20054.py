"""Service module 20054: business logic, no crypto."""


def calculate_total_20054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20054():
    return 'module 20054 handles orders and invoices'
