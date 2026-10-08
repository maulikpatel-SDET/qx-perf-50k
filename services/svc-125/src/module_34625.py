"""Service module 34625: business logic, no crypto."""


def calculate_total_34625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34625():
    return 'module 34625 handles orders and invoices'
