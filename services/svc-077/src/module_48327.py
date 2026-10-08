"""Service module 48327: business logic, no crypto."""


def calculate_total_48327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48327():
    return 'module 48327 handles orders and invoices'
