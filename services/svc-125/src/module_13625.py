"""Service module 13625: business logic, no crypto."""


def calculate_total_13625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13625():
    return 'module 13625 handles orders and invoices'
