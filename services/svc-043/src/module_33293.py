"""Service module 33293: business logic, no crypto."""


def calculate_total_33293(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33293():
    return 'module 33293 handles orders and invoices'
