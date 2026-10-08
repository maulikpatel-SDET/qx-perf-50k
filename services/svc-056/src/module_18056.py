"""Service module 18056: business logic, no crypto."""


def calculate_total_18056(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18056():
    return 'module 18056 handles orders and invoices'
