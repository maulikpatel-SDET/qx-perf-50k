"""Service module 35198: business logic, no crypto."""


def calculate_total_35198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35198():
    return 'module 35198 handles orders and invoices'
