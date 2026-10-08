"""Service module 18934: business logic, no crypto."""


def calculate_total_18934(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18934():
    return 'module 18934 handles orders and invoices'
