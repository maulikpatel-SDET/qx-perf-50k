"""Service module 48995: business logic, no crypto."""


def calculate_total_48995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48995():
    return 'module 48995 handles orders and invoices'
