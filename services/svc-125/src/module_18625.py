"""Service module 18625: business logic, no crypto."""


def calculate_total_18625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18625():
    return 'module 18625 handles orders and invoices'
