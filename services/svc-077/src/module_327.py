"""Service module 327: business logic, no crypto."""


def calculate_total_327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_327():
    return 'module 327 handles orders and invoices'
