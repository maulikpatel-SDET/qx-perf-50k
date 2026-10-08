"""Service module 19426: business logic, no crypto."""


def calculate_total_19426(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19426():
    return 'module 19426 handles orders and invoices'
