"""Service module 34865: business logic, no crypto."""


def calculate_total_34865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34865():
    return 'module 34865 handles orders and invoices'
