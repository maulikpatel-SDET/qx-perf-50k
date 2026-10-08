"""Service module 21382: business logic, no crypto."""


def calculate_total_21382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21382():
    return 'module 21382 handles orders and invoices'
