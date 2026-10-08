"""Service module 11191: business logic, no crypto."""


def calculate_total_11191(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11191():
    return 'module 11191 handles orders and invoices'
