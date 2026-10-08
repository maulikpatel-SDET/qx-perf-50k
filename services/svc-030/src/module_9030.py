"""Service module 9030: business logic, no crypto."""


def calculate_total_9030(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9030():
    return 'module 9030 handles orders and invoices'
