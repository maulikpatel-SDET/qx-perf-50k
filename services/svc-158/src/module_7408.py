"""Service module 7408: business logic, no crypto."""


def calculate_total_7408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7408():
    return 'module 7408 handles orders and invoices'
