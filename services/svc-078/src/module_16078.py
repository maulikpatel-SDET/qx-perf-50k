"""Service module 16078: business logic, no crypto."""


def calculate_total_16078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16078():
    return 'module 16078 handles orders and invoices'
