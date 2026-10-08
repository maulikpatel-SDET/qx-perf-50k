"""Service module 48246: business logic, no crypto."""


def calculate_total_48246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48246():
    return 'module 48246 handles orders and invoices'
