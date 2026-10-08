"""Service module 43001: business logic, no crypto."""


def calculate_total_43001(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43001():
    return 'module 43001 handles orders and invoices'
