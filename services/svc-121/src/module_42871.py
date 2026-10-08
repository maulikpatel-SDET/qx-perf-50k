"""Service module 42871: business logic, no crypto."""


def calculate_total_42871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42871():
    return 'module 42871 handles orders and invoices'
