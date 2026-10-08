"""Service module 26327: business logic, no crypto."""


def calculate_total_26327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26327():
    return 'module 26327 handles orders and invoices'
