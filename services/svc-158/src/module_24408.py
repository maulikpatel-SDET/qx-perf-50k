"""Service module 24408: business logic, no crypto."""


def calculate_total_24408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24408():
    return 'module 24408 handles orders and invoices'
