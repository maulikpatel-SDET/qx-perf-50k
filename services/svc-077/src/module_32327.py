"""Service module 32327: business logic, no crypto."""


def calculate_total_32327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32327():
    return 'module 32327 handles orders and invoices'
