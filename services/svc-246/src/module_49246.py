"""Service module 49246: business logic, no crypto."""


def calculate_total_49246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49246():
    return 'module 49246 handles orders and invoices'
