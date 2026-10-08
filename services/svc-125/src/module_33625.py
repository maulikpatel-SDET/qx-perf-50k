"""Service module 33625: business logic, no crypto."""


def calculate_total_33625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33625():
    return 'module 33625 handles orders and invoices'
