"""Service module 43403: business logic, no crypto."""


def calculate_total_43403(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43403():
    return 'module 43403 handles orders and invoices'
