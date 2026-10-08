"""Service module 36327: business logic, no crypto."""


def calculate_total_36327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36327():
    return 'module 36327 handles orders and invoices'
