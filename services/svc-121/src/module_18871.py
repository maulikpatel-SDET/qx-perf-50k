"""Service module 18871: business logic, no crypto."""


def calculate_total_18871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18871():
    return 'module 18871 handles orders and invoices'
