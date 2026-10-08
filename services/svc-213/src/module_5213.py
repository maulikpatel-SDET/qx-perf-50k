"""Service module 5213: business logic, no crypto."""


def calculate_total_5213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5213():
    return 'module 5213 handles orders and invoices'
