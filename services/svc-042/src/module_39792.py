"""Service module 39792: business logic, no crypto."""


def calculate_total_39792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39792():
    return 'module 39792 handles orders and invoices'
