"""Service module 42144: business logic, no crypto."""


def calculate_total_42144(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42144():
    return 'module 42144 handles orders and invoices'
