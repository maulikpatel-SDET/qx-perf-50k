"""Service module 35428: business logic, no crypto."""


def calculate_total_35428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35428():
    return 'module 35428 handles orders and invoices'
