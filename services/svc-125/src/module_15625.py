"""Service module 15625: business logic, no crypto."""


def calculate_total_15625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15625():
    return 'module 15625 handles orders and invoices'
