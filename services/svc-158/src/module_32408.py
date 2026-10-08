"""Service module 32408: business logic, no crypto."""


def calculate_total_32408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32408():
    return 'module 32408 handles orders and invoices'
