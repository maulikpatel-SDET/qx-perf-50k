"""Service module 17441: business logic, no crypto."""


def calculate_total_17441(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17441():
    return 'module 17441 handles orders and invoices'
