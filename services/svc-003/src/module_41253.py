"""Service module 41253: business logic, no crypto."""


def calculate_total_41253(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41253():
    return 'module 41253 handles orders and invoices'
