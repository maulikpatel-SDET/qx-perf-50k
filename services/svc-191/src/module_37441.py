"""Service module 37441: business logic, no crypto."""


def calculate_total_37441(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37441():
    return 'module 37441 handles orders and invoices'
