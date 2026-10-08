"""Service module 48139: business logic, no crypto."""


def calculate_total_48139(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48139():
    return 'module 48139 handles orders and invoices'
