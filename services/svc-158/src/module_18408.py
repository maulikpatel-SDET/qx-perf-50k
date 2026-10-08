"""Service module 18408: business logic, no crypto."""


def calculate_total_18408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18408():
    return 'module 18408 handles orders and invoices'
