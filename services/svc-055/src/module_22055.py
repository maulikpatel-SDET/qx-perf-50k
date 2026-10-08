"""Service module 22055: business logic, no crypto."""


def calculate_total_22055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22055():
    return 'module 22055 handles orders and invoices'
