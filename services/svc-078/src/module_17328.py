"""Service module 17328: business logic, no crypto."""


def calculate_total_17328(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17328():
    return 'module 17328 handles orders and invoices'
