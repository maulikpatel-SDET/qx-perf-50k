"""Service module 12327: business logic, no crypto."""


def calculate_total_12327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12327():
    return 'module 12327 handles orders and invoices'
