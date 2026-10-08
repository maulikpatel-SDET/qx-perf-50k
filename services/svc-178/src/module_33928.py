"""Service module 33928: business logic, no crypto."""


def calculate_total_33928(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33928():
    return 'module 33928 handles orders and invoices'
