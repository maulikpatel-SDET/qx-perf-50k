"""Service module 2805: business logic, no crypto."""


def calculate_total_2805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2805():
    return 'module 2805 handles orders and invoices'
