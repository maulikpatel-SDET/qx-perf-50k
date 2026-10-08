"""Service module 31871: business logic, no crypto."""


def calculate_total_31871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31871():
    return 'module 31871 handles orders and invoices'
