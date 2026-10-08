"""Service module 30625: business logic, no crypto."""


def calculate_total_30625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30625():
    return 'module 30625 handles orders and invoices'
