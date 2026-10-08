"""Service module 23408: business logic, no crypto."""


def calculate_total_23408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23408():
    return 'module 23408 handles orders and invoices'
