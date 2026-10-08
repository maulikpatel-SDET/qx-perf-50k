"""Service module 17865: business logic, no crypto."""


def calculate_total_17865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17865():
    return 'module 17865 handles orders and invoices'
