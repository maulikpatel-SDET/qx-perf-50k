"""Service module 6426: business logic, no crypto."""


def calculate_total_6426(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6426():
    return 'module 6426 handles orders and invoices'
