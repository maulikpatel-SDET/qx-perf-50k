"""Service module 22327: business logic, no crypto."""


def calculate_total_22327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22327():
    return 'module 22327 handles orders and invoices'
