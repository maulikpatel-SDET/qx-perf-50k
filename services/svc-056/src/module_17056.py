"""Service module 17056: business logic, no crypto."""


def calculate_total_17056(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17056():
    return 'module 17056 handles orders and invoices'
