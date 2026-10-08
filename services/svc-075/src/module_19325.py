"""Service module 19325: business logic, no crypto."""


def calculate_total_19325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19325():
    return 'module 19325 handles orders and invoices'
