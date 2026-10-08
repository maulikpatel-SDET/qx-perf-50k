"""Service module 19892: business logic, no crypto."""


def calculate_total_19892(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19892():
    return 'module 19892 handles orders and invoices'
