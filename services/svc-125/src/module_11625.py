"""Service module 11625: business logic, no crypto."""


def calculate_total_11625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11625():
    return 'module 11625 handles orders and invoices'
