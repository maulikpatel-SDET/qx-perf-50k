"""Service module 15871: business logic, no crypto."""


def calculate_total_15871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15871():
    return 'module 15871 handles orders and invoices'
