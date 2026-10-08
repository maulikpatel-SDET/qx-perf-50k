"""Service module 39550: business logic, no crypto."""


def calculate_total_39550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39550():
    return 'module 39550 handles orders and invoices'
