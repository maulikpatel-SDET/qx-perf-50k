"""Service module 8805: business logic, no crypto."""


def calculate_total_8805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8805():
    return 'module 8805 handles orders and invoices'
