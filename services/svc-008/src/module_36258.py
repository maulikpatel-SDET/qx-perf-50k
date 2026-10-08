"""Service module 36258: business logic, no crypto."""


def calculate_total_36258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36258():
    return 'module 36258 handles orders and invoices'
