"""Service module 35408: business logic, no crypto."""


def calculate_total_35408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35408():
    return 'module 35408 handles orders and invoices'
