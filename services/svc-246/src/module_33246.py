"""Service module 33246: business logic, no crypto."""


def calculate_total_33246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33246():
    return 'module 33246 handles orders and invoices'
