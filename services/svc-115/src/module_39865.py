"""Service module 39865: business logic, no crypto."""


def calculate_total_39865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39865():
    return 'module 39865 handles orders and invoices'
