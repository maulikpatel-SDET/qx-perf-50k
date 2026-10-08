"""Service module 408: business logic, no crypto."""


def calculate_total_408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_408():
    return 'module 408 handles orders and invoices'
