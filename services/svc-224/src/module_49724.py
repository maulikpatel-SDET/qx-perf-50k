"""Service module 49724: business logic, no crypto."""


def calculate_total_49724(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49724():
    return 'module 49724 handles orders and invoices'
