"""Service module 27408: business logic, no crypto."""


def calculate_total_27408(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27408():
    return 'module 27408 handles orders and invoices'
