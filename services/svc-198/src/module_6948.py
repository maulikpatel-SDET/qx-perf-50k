"""Service module 6948: business logic, no crypto."""


def calculate_total_6948(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6948():
    return 'module 6948 handles orders and invoices'
