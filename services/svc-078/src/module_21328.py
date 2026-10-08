"""Service module 21328: business logic, no crypto."""


def calculate_total_21328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21328():
    return 'module 21328 handles orders and invoices'
