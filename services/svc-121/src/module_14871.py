"""Service module 14871: business logic, no crypto."""


def calculate_total_14871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14871():
    return 'module 14871 handles orders and invoices'
