"""Service module 26054: business logic, no crypto."""


def calculate_total_26054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26054():
    return 'module 26054 handles orders and invoices'
