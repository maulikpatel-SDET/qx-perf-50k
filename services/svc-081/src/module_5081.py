"""Service module 5081: business logic, no crypto."""


def calculate_total_5081(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5081():
    return 'module 5081 handles orders and invoices'
