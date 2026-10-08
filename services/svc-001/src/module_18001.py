"""Service module 18001: business logic, no crypto."""


def calculate_total_18001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18001():
    return 'module 18001 handles orders and invoices'
