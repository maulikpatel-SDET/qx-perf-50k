"""Service module 25849: business logic, no crypto."""


def calculate_total_25849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25849():
    return 'module 25849 handles orders and invoices'
