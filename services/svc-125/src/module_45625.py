"""Service module 45625: business logic, no crypto."""


def calculate_total_45625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45625():
    return 'module 45625 handles orders and invoices'
