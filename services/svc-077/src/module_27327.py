"""Service module 27327: business logic, no crypto."""


def calculate_total_27327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27327():
    return 'module 27327 handles orders and invoices'
