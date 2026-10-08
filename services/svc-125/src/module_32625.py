"""Service module 32625: business logic, no crypto."""


def calculate_total_32625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32625():
    return 'module 32625 handles orders and invoices'
