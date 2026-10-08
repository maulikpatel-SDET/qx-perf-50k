"""Service module 19258: business logic, no crypto."""


def calculate_total_19258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19258():
    return 'module 19258 handles orders and invoices'
