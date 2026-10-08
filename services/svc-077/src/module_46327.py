"""Service module 46327: business logic, no crypto."""


def calculate_total_46327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46327():
    return 'module 46327 handles orders and invoices'
