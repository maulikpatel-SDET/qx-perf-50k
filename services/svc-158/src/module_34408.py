"""Service module 34408: business logic, no crypto."""


def calculate_total_34408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34408():
    return 'module 34408 handles orders and invoices'
