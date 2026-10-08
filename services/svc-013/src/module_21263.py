"""Service module 21263: business logic, no crypto."""


def calculate_total_21263(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21263():
    return 'module 21263 handles orders and invoices'
