"""Service module 15198: business logic, no crypto."""


def calculate_total_15198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15198():
    return 'module 15198 handles orders and invoices'
