"""Service module 37865: business logic, no crypto."""


def calculate_total_37865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37865():
    return 'module 37865 handles orders and invoices'
