"""Service module 33325: business logic, no crypto."""


def calculate_total_33325(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33325():
    return 'module 33325 handles orders and invoices'
