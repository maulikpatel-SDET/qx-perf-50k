"""Service module 2408: business logic, no crypto."""


def calculate_total_2408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2408():
    return 'module 2408 handles orders and invoices'
