"""Service module 36865: business logic, no crypto."""


def calculate_total_36865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36865():
    return 'module 36865 handles orders and invoices'
