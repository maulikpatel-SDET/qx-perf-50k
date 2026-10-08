"""Service module 37327: business logic, no crypto."""


def calculate_total_37327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37327():
    return 'module 37327 handles orders and invoices'
