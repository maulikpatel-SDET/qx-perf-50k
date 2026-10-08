"""Service module 625: business logic, no crypto."""


def calculate_total_625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_625():
    return 'module 625 handles orders and invoices'
