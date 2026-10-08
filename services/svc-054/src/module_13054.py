"""Service module 13054: business logic, no crypto."""


def calculate_total_13054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13054():
    return 'module 13054 handles orders and invoices'
