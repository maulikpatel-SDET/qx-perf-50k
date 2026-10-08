"""Service module 26254: business logic, no crypto."""


def calculate_total_26254(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26254():
    return 'module 26254 handles orders and invoices'
