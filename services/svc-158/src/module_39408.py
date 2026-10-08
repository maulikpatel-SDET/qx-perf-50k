"""Service module 39408: business logic, no crypto."""


def calculate_total_39408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39408():
    return 'module 39408 handles orders and invoices'
