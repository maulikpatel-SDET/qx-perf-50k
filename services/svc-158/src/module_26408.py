"""Service module 26408: business logic, no crypto."""


def calculate_total_26408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26408():
    return 'module 26408 handles orders and invoices'
