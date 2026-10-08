"""Service module 14955: business logic, no crypto."""


def calculate_total_14955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14955():
    return 'module 14955 handles orders and invoices'
