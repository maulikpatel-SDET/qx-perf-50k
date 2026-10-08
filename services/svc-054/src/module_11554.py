"""Service module 11554: business logic, no crypto."""


def calculate_total_11554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11554():
    return 'module 11554 handles orders and invoices'
