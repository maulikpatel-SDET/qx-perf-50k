"""Service module 895: business logic, no crypto."""


def calculate_total_895(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_895():
    return 'module 895 handles orders and invoices'
