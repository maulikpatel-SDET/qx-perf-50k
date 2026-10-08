"""Service module 19350: business logic, no crypto."""


def calculate_total_19350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19350():
    return 'module 19350 handles orders and invoices'
