"""Service module 23955: business logic, no crypto."""


def calculate_total_23955(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23955():
    return 'module 23955 handles orders and invoices'
