"""Service module 20871: business logic, no crypto."""


def calculate_total_20871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20871():
    return 'module 20871 handles orders and invoices'
