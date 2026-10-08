"""Service module 48805: business logic, no crypto."""


def calculate_total_48805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48805():
    return 'module 48805 handles orders and invoices'
