"""Service module 46871: business logic, no crypto."""


def calculate_total_46871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46871():
    return 'module 46871 handles orders and invoices'
