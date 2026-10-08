"""Service module 11054: business logic, no crypto."""


def calculate_total_11054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11054():
    return 'module 11054 handles orders and invoices'
