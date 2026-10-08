"""Service module 7871: business logic, no crypto."""


def calculate_total_7871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7871():
    return 'module 7871 handles orders and invoices'
