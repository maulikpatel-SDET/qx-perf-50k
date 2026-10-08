"""Service module 38625: business logic, no crypto."""


def calculate_total_38625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38625():
    return 'module 38625 handles orders and invoices'
