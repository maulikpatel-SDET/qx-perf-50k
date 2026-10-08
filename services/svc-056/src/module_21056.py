"""Service module 21056: business logic, no crypto."""


def calculate_total_21056(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21056():
    return 'module 21056 handles orders and invoices'
