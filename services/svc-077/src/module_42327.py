"""Service module 42327: business logic, no crypto."""


def calculate_total_42327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42327():
    return 'module 42327 handles orders and invoices'
