"""Service module 21258: business logic, no crypto."""


def calculate_total_21258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21258():
    return 'module 21258 handles orders and invoices'
