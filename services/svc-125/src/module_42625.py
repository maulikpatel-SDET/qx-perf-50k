"""Service module 42625: business logic, no crypto."""


def calculate_total_42625(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42625():
    return 'module 42625 handles orders and invoices'
