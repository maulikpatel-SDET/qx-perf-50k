"""Service module 24230: business logic, no crypto."""


def calculate_total_24230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24230():
    return 'module 24230 handles orders and invoices'
