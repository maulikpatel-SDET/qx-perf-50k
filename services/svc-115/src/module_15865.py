"""Service module 15865: business logic, no crypto."""


def calculate_total_15865(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15865():
    return 'module 15865 handles orders and invoices'
