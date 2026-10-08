"""Service module 15408: business logic, no crypto."""


def calculate_total_15408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15408():
    return 'module 15408 handles orders and invoices'
