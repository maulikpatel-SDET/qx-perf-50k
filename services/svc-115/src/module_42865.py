"""Service module 42865: business logic, no crypto."""


def calculate_total_42865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42865():
    return 'module 42865 handles orders and invoices'
