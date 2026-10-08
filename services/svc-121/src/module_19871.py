"""Service module 19871: business logic, no crypto."""


def calculate_total_19871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19871():
    return 'module 19871 handles orders and invoices'
