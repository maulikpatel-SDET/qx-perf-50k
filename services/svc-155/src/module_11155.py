"""Service module 11155: business logic, no crypto."""


def calculate_total_11155(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11155():
    return 'module 11155 handles orders and invoices'
