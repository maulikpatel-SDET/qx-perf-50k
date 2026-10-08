"""Service module 4805: business logic, no crypto."""


def calculate_total_4805(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4805():
    return 'module 4805 handles orders and invoices'
