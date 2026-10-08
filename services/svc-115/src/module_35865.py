"""Service module 35865: business logic, no crypto."""


def calculate_total_35865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35865():
    return 'module 35865 handles orders and invoices'
