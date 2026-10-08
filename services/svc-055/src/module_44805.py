"""Service module 44805: business logic, no crypto."""


def calculate_total_44805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44805():
    return 'module 44805 handles orders and invoices'
