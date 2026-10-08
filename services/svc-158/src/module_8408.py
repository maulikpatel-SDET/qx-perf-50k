"""Service module 8408: business logic, no crypto."""


def calculate_total_8408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8408():
    return 'module 8408 handles orders and invoices'
