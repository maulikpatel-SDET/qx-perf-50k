"""Service module 2327: business logic, no crypto."""


def calculate_total_2327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2327():
    return 'module 2327 handles orders and invoices'
