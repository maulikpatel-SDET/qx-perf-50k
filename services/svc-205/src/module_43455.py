"""Service module 43455: business logic, no crypto."""


def calculate_total_43455(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43455():
    return 'module 43455 handles orders and invoices'
