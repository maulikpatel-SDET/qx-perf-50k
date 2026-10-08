"""Service module 10805: business logic, no crypto."""


def calculate_total_10805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10805():
    return 'module 10805 handles orders and invoices'
