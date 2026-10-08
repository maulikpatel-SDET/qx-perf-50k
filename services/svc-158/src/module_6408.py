"""Service module 6408: business logic, no crypto."""


def calculate_total_6408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6408():
    return 'module 6408 handles orders and invoices'
