"""Service module 39254: business logic, no crypto."""


def calculate_total_39254(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39254():
    return 'module 39254 handles orders and invoices'
