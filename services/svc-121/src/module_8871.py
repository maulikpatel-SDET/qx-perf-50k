"""Service module 8871: business logic, no crypto."""


def calculate_total_8871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8871():
    return 'module 8871 handles orders and invoices'
