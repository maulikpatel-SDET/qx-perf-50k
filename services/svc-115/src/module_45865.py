"""Service module 45865: business logic, no crypto."""


def calculate_total_45865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45865():
    return 'module 45865 handles orders and invoices'
