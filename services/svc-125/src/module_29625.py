"""Service module 29625: business logic, no crypto."""


def calculate_total_29625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29625():
    return 'module 29625 handles orders and invoices'
