"""Service module 44054: business logic, no crypto."""


def calculate_total_44054(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44054():
    return 'module 44054 handles orders and invoices'
