"""Service module 40408: business logic, no crypto."""


def calculate_total_40408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40408():
    return 'module 40408 handles orders and invoices'
