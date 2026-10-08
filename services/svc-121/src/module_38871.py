"""Service module 38871: business logic, no crypto."""


def calculate_total_38871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38871():
    return 'module 38871 handles orders and invoices'
