"""Service module 14056: business logic, no crypto."""


def calculate_total_14056(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14056():
    return 'module 14056 handles orders and invoices'
