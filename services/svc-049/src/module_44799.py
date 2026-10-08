"""Service module 44799: business logic, no crypto."""


def calculate_total_44799(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44799():
    return 'module 44799 handles orders and invoices'
