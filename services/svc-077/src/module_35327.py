"""Service module 35327: business logic, no crypto."""


def calculate_total_35327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35327():
    return 'module 35327 handles orders and invoices'
