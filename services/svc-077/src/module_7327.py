"""Service module 7327: business logic, no crypto."""


def calculate_total_7327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7327():
    return 'module 7327 handles orders and invoices'
