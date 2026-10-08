"""Service module 4230: business logic, no crypto."""


def calculate_total_4230(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4230():
    return 'module 4230 handles orders and invoices'
